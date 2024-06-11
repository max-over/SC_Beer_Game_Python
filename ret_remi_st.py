
# -*- coding: utf-8 -*-


from remi import start, App
import ret_remi_st_gui
from network3 import Network
import pickle
from xlwt import Workbook
import time

DISABLED_COLOR = "rgb(200,200,200)"
ENABLED_COLOR = "rgb(0,200,200)"
HOLDINGRATE = 4
BACKLOGRATE = 10
LEADTIMEUP = 2
INVENTORY = 20


class ProcessData:
    def __init__(self, data_id, data_list, data_leadtimeup):
        self.data_id = data_id
        self.data_list = data_list
        self.data_leadtimeup = data_leadtimeup


class ret_remi(App):

    def __init__(self, *args, **kwargs):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        self.xtime = str(round(time.time()))
        self.data = ""
        self.current_period = 0
        self.current_demand = 0
        self.inventory = INVENTORY
        self.leadtimeup = LEADTIMEUP
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
        self.sheet_ret = self.wb.add_sheet("Retailer")
        self.sheet_ret.write(0, 0, "Period")
        self.sheet_ret.write(0, 1, "Demand")
        self.sheet_ret.write(0, 2, "Order")
        self.sheet_ret.write(0, 3, "Shipment")
        self.sheet_ret.write(0, 4, "Inventory")
        self.sheet_ret.write(0, 5, "Total_Costs")
        self.sheet_ret.write(0, 6, "Lost sales")
        self.sheet_ret.write(0, 7, "SL")
        self.sheet_ret.write(0, 8, "Inventory_Costs")
        self.sheet_ret.write(0, 9, "Lost_sales_Costs")
        if not 'editing_mode' in kwargs.keys():
            super(ret_remi, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        # idle function called every update cycle
        pass
    
    def main(self):
        self.root = ret_remi_st_gui.construct_ui(self)
        return self.root

    def on_button_ret_connect_pressed(self, textEditPassRet, textEditServerRet, textEditPortRet, label_ret_info,
                                      button_ret_update, button_ret_disconnect, widget):

        password = textEditPassRet.get_text()
        server = textEditServerRet.get_text()
        port = int(textEditPortRet.get_text())
        if self.is_valid_password(password):
            self.n = Network(server, port)
            self.run = True
            print(server)
            print(port)
            try:
                self.n.send(pickle.dumps(ProcessData("get_ret", [0], 0)))
                label_ret_info.set_text(f"Retailer connected to: {server}_{port}")
                label_ret_info.css_visibility = "visible"
            except:
                self.run = False
            self._enable_button(button_ret_update)
            self._disable_button(widget)
            self._enable_button(button_ret_disconnect)
            textEditPassRet.set_text("")
        else:
            pass

    def is_valid_password(self, password):
        return password == "1"

    def _enable_button(self, button):
        button.set_enabled(True)
        button.css_background_color = ENABLED_COLOR

    def _disable_button(self, button):
        button.set_enabled(False)
        button.css_background_color = DISABLED_COLOR

    def on_button_ret_disconnect_pressed(self, button_ret_connect, label_ret_info, widget):
        self.n.send(pickle.dumps(ProcessData("disconnect", [0], 0)))
        self._enable_button(button_ret_connect)
        self._disable_button(widget)
        label_ret_info.set_text("Disconnected from server")

    def on_button_ret_update_pressed(self, button_ret_order, label_ret_period, textEditPortRet, label_ret_costs,
                                     label_ret_demand, label_ret_sl, label_ret_inventory, label_ret_backlog,
                                     label_ret_status, widget):
        server_period = self.n.send(pickle.dumps(ProcessData("upd_ret_period", [0], self.current_period)))

        if int(server_period) > self.current_period:
            self._enable_button(button_ret_order)
            self.current_period = int(server_period)
            label_ret_period.set_text(f"Current Period: {server_period}")
            self.sheet_ret.write(int(self.current_period), 0, int(self.current_period))
            self.wb.save(f'ret_stat{textEditPortRet.get_text()}_{self.xtime}.xls')

            if self.current_period > 1:
                shipment = self.n.send(pickle.dumps(ProcessData("upd_ret_distr_shipment",
                                                                [self.current_period], self.leadtimeup)))
                self.update_backlog_and_inventory_shipment(shipment)

            demand = self.n.send(pickle.dumps(ProcessData("upd_ret_cust_demand", [0], 0)))
            self.current_demand = demand.data_leadtimeup
            print(self.current_demand)

            self.update_costs()
            self.update_backlog_and_inventory_demand()

            self.sl = 1 - self.backlogcount / self.current_period

            label_ret_costs.set_text(f"Costs(total): {self.costs}")
            label_ret_demand.set_text(f"Demand: {self.current_demand}")
            label_ret_sl.set_text(f"Lost sales periods: {self.backlogcount}")
            label_ret_inventory.set_text(f"Inventory: {self.inventory}")
            label_ret_backlog.set_text(f"Lost sales(total): {self.backlogtotal}")

            self.sheet_ret.write(int(self.current_period), 1, int(self.current_demand))
            self.sheet_ret.write(int(self.current_period), 4, int(self.inventory))
            self.sheet_ret.write(int(self.current_period), 5, int(self.costs))
            self.sheet_ret.write(int(self.current_period), 6, int(self.backlogtotal))
            self.sheet_ret.write(int(self.current_period), 7, float(self.sl))
            self.sheet_ret.write(int(self.current_period), 8, float(self.inventorycosts))
            self.sheet_ret.write(int(self.current_period), 9, float(self.backlogcosts))
            self.wb.save(f'ret_stat{textEditPortRet.get_text()}_{self.xtime}.xls')

        status_text = self.n.send(pickle.dumps(ProcessData("check_status_node", [0], 0)))
        label_ret_status.set_text(status_text)

    def update_backlog_and_inventory_shipment(self, shipment):
        if shipment.data_list != "":
            if self.backlog > int(shipment.data_list):
                self.backlog -= int(shipment.data_list)
                self.inventory = 0
            else:
                inv_remaining = int(shipment.data_list) - self.backlog
                self.backlog = 0
                self.inventory += inv_remaining

    def update_backlog_and_inventory_demand(self):
        if int(self.current_demand) > int(self.inventory):
            self.backlog = int(self.current_demand) - int(self.inventory)
            self.backlogtotal += self.backlog
            self.inventory = 0
        else:
            self.inventory -= int(self.current_demand)
            self.backlog = 0
        if self.backlog > 0:
            self.backlogcount += 1

    def update_costs(self):
        self.inventorycosts += self.inventory * self.holdingrate
        self.backlogcosts = self.backlogtotal * self.backlograte
        self.costs = self.inventorycosts + self.backlogcosts

    def on_button_ret_place_order_pressed(self, textEditOrderRetailer, textEditPortRet, button_ret_order, widget):
        try:
            ret_order = int(textEditOrderRetailer.get_text())
            if ret_order >= 0:
                self.n.send(pickle.dumps(ProcessData("ret_order", [0], ret_order)))
                self.sheet_ret.write(int(self.current_period), 2, int(ret_order))
                self.wb.save(f'ret_stat{textEditPortRet.get_text()}_{self.xtime}.xls')
                self._disable_button(button_ret_order)
            else:
                ret_order = 0
        except ValueError:
            ret_order = 0

        textEditOrderRetailer.set_text(str(ret_order))


# Configuration
configuration = {'config_project_name': 'ret_remi', 'config_address': '0.0.0.0', 'config_port': 8089, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(ret_remi, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
