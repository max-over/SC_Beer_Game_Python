
# -*- coding: utf-8 -*-


from remi import start, App
import plant_remi_st_gui
from network3 import Network
import pickle
from xlwt import Workbook
import time

DISABLED_COLOR = "rgb(200,200,200)"
ENABLED_COLOR = "rgb(184,184,105)"
HOLDINGRATE_RAW = 1
HOLDINGRATE_FINISHED = 2
BACKLOGRATE = 4
LEADTIMEUP = 2
INVENTORY_RAW = 25
INVENTORY_FINISHED = 20
PRODUCTIONTIME = 2

class ProcessData:
    def __init__(self, data_id, data_list, data_leadtimeup):
        self.data_id = data_id
        self.data_list = data_list
        self.data_leadtimeup = data_leadtimeup


class plant_remi(App):

    def __init__(self, *args, **kwargs):
        self.xtime = str(round(time.time()))
        self.shipment_plant_queue = []
        self.production_plant_queue = []
        self.supplier_order = 0
        self.produced_lot = 0
        self.current_period = 0
        self.current_demand = 0
        self.inventory_raw = INVENTORY_RAW
        self.inventory_finished = INVENTORY_FINISHED
        self.leadtimeup = LEADTIMEUP
        self.sl = 1.00
        self.costs = 0
        self.backlog = 0
        self.backlogtotal = 0
        self.holdingrate_raw = HOLDINGRATE_RAW
        self.holdingrate_finished = HOLDINGRATE_FINISHED
        self.backlograte = BACKLOGRATE
        self.backlogcount = 0
        self.productiontime = PRODUCTIONTIME
        self.prodshipmentList = []
        self.backlogcosts = 0
        self.inventorycosts = 0
        self.wb = Workbook()
        self.sheet_plant = self.wb.add_sheet("Plant")
        self.sheet_plant.write(0, 0, "Period")
        self.sheet_plant.write(0, 1, "Demand")
        self.sheet_plant.write(0, 2, "Order")
        self.sheet_plant.write(0, 3, "Shipment")
        self.sheet_plant.write(0, 4, "Inventory_raw")
        self.sheet_plant.write(0, 5, "Inventory_finished")
        self.sheet_plant.write(0, 6, "Production")
        self.sheet_plant.write(0, 7, "Total_costs")
        self.sheet_plant.write(0, 8, "Backlog")
        self.sheet_plant.write(0, 9, "SL")
        self.sheet_plant.write(0, 10, "Inventory_costs")
        self.sheet_plant.write(0, 11, "Lost_sales_costs")
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(plant_remi, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        # idle function called every update cycle
        pass
    
    def main(self):
        self.root = plant_remi_st_gui.construct_ui(self)
        return self.root

    def is_valid_password(self, password):
        return password == "1"

    def _enable_button(self, button):
        button.set_enabled(True)
        button.css_background_color = ENABLED_COLOR

    def _disable_button(self, button):
        button.set_enabled(False)
        button.css_background_color = DISABLED_COLOR

    def on_button_plant_disconnect_pressed(self, button_plant_connect, label_plant_info, widget):
        self.n.send(pickle.dumps(ProcessData("disconnect", [0], 0)))
        self._enable_button(button_plant_connect)
        self._disable_button(widget)
        label_plant_info.set_text("Disconnected from server")

    def on_button_plant_produce_pressed(self, textEditProdlotPlant, label_plant_inventory_raw, button_plant_order,
                                        button_plant_produce, widget):
        try:
            prodlot = int(textEditProdlotPlant.get_text())
            prodlot = min(prodlot, int(self.inventory_raw)) if prodlot >= 0 else 0
            self.n.send(pickle.dumps(ProcessData("plant_prodlot", [0], prodlot)))
            self.inventory_raw -= prodlot
            label_plant_inventory_raw.set_text(f"Inventory raw: {self.inventory_raw}")
            self.production_plant_queue.append([prodlot, self.current_period + self.productiontime])
            self._disable_button(button_plant_produce)
        except ValueError:
            prodlot = 0
        textEditProdlotPlant.set_text(str(prodlot))
        self._enable_button(button_plant_order)

    def on_button_plant_connect_pressed(self, textEditPassPlant, textEditServerPlant, textEditPortPlant,
                                        label_plant_info, button_plant_update, button_plant_disconnect, widget):
        password = textEditPassPlant.get_text()
        server = textEditServerPlant.get_text()
        port = int(textEditPortPlant.get_text())
        if self.is_valid_password(password):
            self.n = Network(server, port)
            self.run = True
            print(server)
            print(port)
            try:
                self.n.send(pickle.dumps(ProcessData("get_plant", [0], 0)))
                label_plant_info.set_text(f"Plant connected to: {server}_{port}")
                label_plant_info.css_visibility = "visible"
            except:
                self.run = False
            self._enable_button(button_plant_update)
            self._disable_button(widget)
            self._enable_button(button_plant_disconnect)
            textEditPassPlant.set_text("")
        else:
            pass

    def on_button_plant_update_pressed(self, label_plant_demand, button_plant_shipment, label_plant_period,
                                       textEditPortPlant, label_plant_costs, label_plant_inventory_finished,
                                       label_plant_inventory_raw, label_plant_backlog, label_plant_status, widget):
        server_period = self.n.send(pickle.dumps(ProcessData("upd_ret_period", [0], self.current_period)))
        whole_demand = self.n.send(pickle.dumps(ProcessData("upd_whole_plant_demand", [0], 0)))
        self.current_demand = whole_demand.data_leadtimeup
        label_plant_demand.set_text(f"Demand: {self.current_demand}")
        if int(server_period) == 0:
            label_plant_demand.set_text("Demand: no data")
        if int(server_period) > self.current_period:
            self._enable_button(button_plant_shipment)
            self.current_period = int(server_period)
            label_plant_period.set_text(f"Current Period: {self.current_period}")
            self.sheet_plant.write(int(self.current_period), 0, int(self.current_period))
            self.wb.save(f"plant_stat{textEditPortPlant.get_text()}_{self.xtime}.xls")

            self.supplier_order = next((
                int(row[0]) for row in self.shipment_plant_queue if int(row[1]) == self.current_period - self.leadtimeup
            ), 0)

            self.inventory_raw += self.supplier_order

            if len(self.shipment_plant_queue) > 20:
                self.shipment_plant_queue.pop(0)

            self.produced_lot = next((
                int(row[0]) for row in self.production_plant_queue if int(row[1]) == self.current_period
            ), 0)

            if len(self.production_plant_queue) > 20:
                self.production_plant_queue.pop(0)

            self.inventory_finished += self.produced_lot

            self.update_costs()

            self.sheet_plant.write(int(self.current_period), 10, float(self.inventorycosts))
            self.sheet_plant.write(int(self.current_period), 11, float(self.backlogcosts))
            label_plant_costs.set_text(f"Costs(total): {self.costs}")
            label_plant_inventory_finished.set_text(f"Inventory finished: {self.inventory_finished}")
            label_plant_inventory_raw.set_text(f"Inventory raw: {self.inventory_raw}")
            label_plant_backlog.set_text(f"Backlog(total): {self.backlogtotal}")

        status_text = self.n.send(pickle.dumps(ProcessData("check_status_node", [0], 0)))
        label_plant_status.set_text(status_text)

    def update_costs(self):
        self.inventorycosts += self.inventory_raw * self.holdingrate_raw + self.inventory_finished * self.holdingrate_finished
        self.backlogcosts += self.backlogtotal * self.backlograte
        self.costs = self.inventorycosts + self.backlogcosts

    def on_button_plant_shipment_pressed(self, textEditShipmentPlant, label_plant_sl, textEditPortPlant,
                                         label_plant_inventory_finished, label_plant_backlog, button_plant_shipment,
                                          button_plant_produce, widget):
        try:
            prodshipment = int(textEditShipmentPlant.get_text())
            prodshipment = min(prodshipment, self.inventory_finished, self.current_demand + self.backlogtotal)
            prodshipment = max(prodshipment, 0) if prodshipment >= 0 else 0

            self.update_backlog_and_inventory_demand(prodshipment)
            self.sl = 1 - self.backlogcount / self.current_period

            self.n.send(pickle.dumps(ProcessData("plant_shipment", [0], prodshipment)))

            self.sheet_plant.write(int(self.current_period), 1, int(self.current_demand))
            self.sheet_plant.write(int(self.current_period), 3, prodshipment)
            self.sheet_plant.write(int(self.current_period), 4, int(self.inventory_raw))
            self.sheet_plant.write(int(self.current_period), 5, int(self.inventory_finished))
            self.sheet_plant.write(int(self.current_period), 6, int(self.produced_lot))
            self.sheet_plant.write(int(self.current_period), 7, int(self.costs))
            self.sheet_plant.write(int(self.current_period), 8, int(self.backlog))
            self.sheet_plant.write(int(self.current_period), 9, float(self.sl))
            self.wb.save(f"plant_stat{textEditPortPlant.get_text()}_{self.xtime}.xls")
            label_plant_sl.set_text(f"Backlog periods: {self.backlogcount}")
            label_plant_inventory_finished.set_text(f"Inventory finished: {self.inventory_finished}")
            label_plant_backlog.set_text(f"Backlog(total): {self.backlogtotal}")
            self._disable_button(button_plant_shipment)
            self._enable_button(button_plant_produce)
        except ValueError:
            prodshipment = 0
        textEditShipmentPlant.set_text(str(prodshipment))

    def update_backlog_and_inventory_demand(self, prodshipment):
        if int(self.current_demand) > int(prodshipment):
            self.backlog = int(self.current_demand) - int(prodshipment)
            self.backlogtotal += - (prodshipment - self.current_demand)
            self.backlogcount += 1
            self.inventory_finished = 0
        else:
            self.backlogtotal = self.backlogtotal - (prodshipment - self.current_demand)
            self.wb.save(f"plant_stat{textEditPortPlant.get_text()}_{self.xtime}.xls")
            self.inventory_finished += - int(prodshipment)

    def on_button_plant_order_pressed(self, textEditOrderPlant, button_plant_order, textEditPortPlant, widget):
        try:
            prodorder = int(textEditOrderPlant.get_text())
            if prodorder >= 0:
                self.n.send(pickle.dumps(ProcessData("plant_order", [0], prodorder)))
                self.shipment_plant_queue.append((prodorder, self.current_period))
                self.sheet_plant.write(int(self.current_period), 2, int(prodorder))
                self.wb.save(f"plant_stat{textEditPortPlant.get_text()}_{self.xtime}.xls")
                self._disable_button(button_plant_order)
            else:
                prodorder = 0
        except ValueError:
            prodorder = 0
        textEditOrderPlant.set_text(str(prodorder))


# Configuration
configuration = {'config_project_name': 'plant_remi', 'config_address': '0.0.0.0', 'config_port': 8087, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(plant_remi, address=configuration['config_address'], port=configuration['config_port'],
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
