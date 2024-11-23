
# -*- coding: utf-8 -*-

from remi import start, App
import distr_remi_st_gui
from network3 import Network
import pickle
from xlwt import Workbook
import time

DISABLED_COLOR = "rgb(200,200,200)"
ENABLED_COLOR = "rgb(158,176,253)"
HOLDINGRATE = 2
BACKLOGRATE = 4
LEADTIMEUP = 2
INVENTORY = 20


class ProcessData:
    def __init__(self, data_id, data_list, data_leadtimeup):
        self.data_id = data_id
        self.data_list = data_list
        self.data_leadtimeup = data_leadtimeup


class distr_remi(App):

    def __init__(self, *args, **kwargs):
        self.xtime = str(round(time.time()))
        self.current_period = 0
        self.current_demand = 0
        self.inventory = INVENTORY
        self.leadtimeup = LEADTIMEUP
        self.leadtimedown = 2
        self.sl = 1.00
        self.costs = 0
        self.backlog = 0
        self.holdingrate = HOLDINGRATE
        self.backlograte = BACKLOGRATE
        self.backlogcount = 0
        self.backlogtotal = 0
        self.inventorycosts = 0
        self.backlogcosts = 0
        self.wb = Workbook()
        self.sheet_distr = self.wb.add_sheet("Distributor")
        self.sheet_distr.write(0, 0, "Period")
        self.sheet_distr.write(0, 1, "Demand")
        self.sheet_distr.write(0, 2, "Order")
        self.sheet_distr.write(0, 3, "Shipment")
        self.sheet_distr.write(0, 4, "Inventory")
        self.sheet_distr.write(0, 5, "Total_Costs")
        self.sheet_distr.write(0, 6, "Backlog")
        self.sheet_distr.write(0, 7, "SL")
        self.sheet_distr.write(0, 8, "Inventory_Costs")
        self.sheet_distr.write(0, 9, "Backlog_Costs")
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(distr_remi, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        # idle function called every update cycle
        pass
    
    def main(self):
        self.root = distr_remi_st_gui.construct_ui(self)
        return self.root

    def is_valid_password(self, password):
        return password == "1"

    def _enable_button(self, button):
        button.set_enabled(True)
        button.css_background_color = ENABLED_COLOR

    def _disable_button(self, button):
        button.set_enabled(False)
        button.css_background_color = DISABLED_COLOR

    def on_button_distr_disconnect_pressed(self, button_distr_connect, label_distr_info, widget):
        self.n.send(pickle.dumps(ProcessData("disconnect", [0], 0)))
        self._enable_button(button_distr_connect)
        self._disable_button(widget)
        label_distr_info.set_text("Disconnected from server")

    def on_button_distr_connect_pressed(self, textEditPassDistr, textEditServerDistr, textEditPortDistr,
                                        label_distr_info, button_distr_update, button_distr_disconnect, widget):
        password = textEditPassDistr.get_text()
        server = textEditServerDistr.get_text()
        port = int(textEditPortDistr.get_text())
        if self.is_valid_password(password):
            self.n = Network(server, port)
            self.run = True
            print(server)
            print(port)
            try:
                self.n.send(pickle.dumps(ProcessData("get_distr", [0], 0)))
                label_distr_info.set_text(f"Distributor connected to: {server}_{port}")
                label_distr_info.css_visibility = "visible"
                self.current_period = self.n.send(pickle.dumps(ProcessData("get_distr_lastperiod", [0], self.current_period)))
                self.inventorycosts = self.n.send(pickle.dumps(ProcessData("get_distr_inventorycosts", [0], 0)))
                self.backlogcosts = self.n.send(pickle.dumps(ProcessData("get_distr_backlogcosts", [0], 0)))
                self.backlogtotal = self.n.send(pickle.dumps(ProcessData("get_distr_backlogtotal", [0], 0)))
                self.costs = self.n.send(pickle.dumps(ProcessData("get_distr_costs", [0], 0)))
                if self.current_period > 0:
                    self.inventory = self.n.send(pickle.dumps(ProcessData("get_distr_inventory", [0], 0)))
                self._disable_button(button_distr_order)
            except:
                self.run = False
            self._enable_button(button_distr_update)
            self._disable_button(widget)
            self._enable_button(button_distr_disconnect)
            textEditPassDistr.set_text("")
        else:
            pass

    def on_button_distr_update_pressed(self, button_distr_shipment, label_distr_period, textEditPortDistr, label_distr_costs,
                                       label_distr_demand, label_distr_inventory, label_distr_backlog,
                                       label_distr_status, widget):
        server_period = self.n.send(pickle.dumps(ProcessData("upd_ret_period", [0], self.current_period)))
        ret_demand = self.n.send(pickle.dumps(ProcessData("upd_ret_distr_demand", [0], 0)))
        # print(str(ret_demand.data_leadtimeup))
        self.current_demand = ret_demand.data_leadtimeup
        label_distr_demand.set_text(f"Demand: {self.current_demand}")
        if int(server_period) == 0:
            label_distr_demand.set_text("Demand: no data")

        if int(server_period) > self.current_period:
            self._enable_button(button_distr_shipment)
            self.current_period = int(server_period)
            label_distr_period.set_text(f"Current Period: {self.current_period}")
            self.sheet_distr.write(int(self.current_period), 0, int(self.current_period))
            self.wb.save(f"distr_stat{textEditPortDistr.get_text()}_{self.xtime}.xls")

            if self.current_period > 1:
                shipment = self.n.send(
                    pickle.dumps(ProcessData("upd_distr_whole_shipment", [self.current_period], self.leadtimeup)))
                if shipment.data_list != "":
                    self.inventory += int(shipment.data_list)

            self.update_costs()

            self.sheet_distr.write(int(self.current_period), 8, float(self.inventorycosts))
            self.sheet_distr.write(int(self.current_period), 9, float(self.backlogcosts))

            label_distr_costs.set_text(f"Costs(total): {self.costs}")
            label_distr_inventory.set_text(f"Inventory: {self.inventory}")
            label_distr_backlog.set_text(f"Backlog(total): {self.backlogtotal}")

        status_text = self.n.send(pickle.dumps(ProcessData("check_status_node", [0], 0)))
        label_distr_status.set_text(status_text)

    def update_costs(self):
        self.inventorycosts += self.inventory * self.holdingrate
        self.backlogcosts += self.backlogtotal * self.backlograte
        self.costs = self.inventorycosts + self.backlogcosts

    def on_button_distr_shipment_pressed(self, textEditShipmentDistributor, label_distr_inventory, label_distr_sl,
                                         textEditPortDistr, button_distr_shipment, button_distr_order,
                                         label_distr_backlog, widget):
        try:
            distrshipment = int(textEditShipmentDistributor.get_text())
            distrshipment = min(distrshipment, self.inventory, self.current_demand + self.backlogtotal)
            distrshipment = max(distrshipment, 0) if distrshipment >= 0 else 0

            self.update_backlog_and_inventory_demand(distrshipment)

            self.n.send(pickle.dumps(ProcessData("distr_shipment", [0], distrshipment)))
            self.sl = 1 - self.backlogcount / self.current_period

            self.sheet_distr.write(int(self.current_period), 1, int(self.current_demand))
            self.sheet_distr.write(int(self.current_period), 3, int(distrshipment))
            self.sheet_distr.write(int(self.current_period), 4, int(self.inventory))
            self.sheet_distr.write(int(self.current_period), 5, int(self.costs))
            self.sheet_distr.write(int(self.current_period), 6, int(self.backlogtotal))
            self.sheet_distr.write(int(self.current_period), 7, float(self.sl))
            self.wb.save(f"distr_stat{textEditPortDistr.get_text()}_{self.xtime}.xls")
            self._disable_button(button_distr_shipment)
            label_distr_sl.set_text(f"Backlog periods: {self.backlogcount}")
            label_distr_inventory.set_text(f"Inventory: {self.inventory}")
            label_distr_backlog.set_text(f"Backlog(total): {self.backlogtotal}")
            self._enable_button(button_distr_order)

        except ValueError:
            distrshipment = 0
        textEditShipmentDistributor.set_text(str(distrshipment))

    def update_backlog_and_inventory_demand(self, distrshipment):
        self.backlogtotal += self.current_demand - distrshipment
        if int(self.current_demand) > distrshipment:
            self.backlogcount += 1
            self.inventory = 0
        else:
            self.inventory += - distrshipment

    def on_button_distr_order_pressed(self, textEditOrderDistributor, button_distr_order, textEditPortDistr, widget):
        try:
            distr_order = int(textEditOrderDistributor.get_text())
            if distr_order >= 0:
                self.n.send(pickle.dumps(ProcessData("distr_order", [0], distr_order)))
                self.n.send(pickle.dumps(ProcessData("upd_distr_inventorycosts", [0], self.inventorycosts)))
                self.n.send(pickle.dumps(ProcessData("upd_distr_backlogcosts", [0], self.backlogcosts)))
                self.n.send(pickle.dumps(ProcessData("upd_distr_costs", [0], self.costs)))
                self.n.send(pickle.dumps(ProcessData("upd_distr_lastperiod", [0], self.current_period)))
                self.n.send(pickle.dumps(ProcessData("upd_distr_backlogtotal", [0], self.backlogtotal)))
                self.n.send(pickle.dumps(ProcessData("upd_distr_inventory", [0], self.inventory)))
                self.sheet_distr.write(int(self.current_period), 2, int(distr_order))
                self.wb.save(f'distr_stat{textEditPortDistr.get_text()}_{self.xtime}.xls')
                self._disable_button(button_distr_order)

            else:
                distr_order = 0
        except ValueError:
            distr_order = 0

        textEditOrderDistributor.set_text(str(distr_order))


# Configuration
configuration = {'config_project_name': 'distr_remi', 'config_address': '0.0.0.0', 'config_port': 8085, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(distr_remi, address=configuration['config_address'], port=configuration['config_port'],
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
