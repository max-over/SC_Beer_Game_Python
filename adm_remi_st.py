
# -*- coding: utf-8 -*-

from remi import start, App
import adm_remi_st_gui

from network3 import Network
import pickle
import time

DISABLED_COLOR = "rgb(200,200,200)"
ENABLED_COLOR = "rgb(100,100,100)"


class ProcessData:
    def __init__(self, data_id, data_list, data_leadtimeup):
        self.data_id = data_id
        self.data_list = data_list
        self.data_leadtimeup = data_leadtimeup


class adm_remi(App):
    xtime = str(round(time.time()))

    def __init__(self, *args, **kwargs):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(adm_remi, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        # idle function called every update cycle
        pass

    def main(self):
        self.root = adm_remi_st_gui.construct_ui(self)
        self.current_period = 1
        self.adm_period = 0
        return self.root

    def on_button_adm_connect_pressed(self, textEditPassAdm, textEditServerAdm, textEditPortAdm, label_adm_info,
                                      button_adm_disconnect, button_adm_setperiod, widget):
        password = textEditPassAdm.get_text()
        server = textEditServerAdm.get_text()
        port = int(textEditPortAdm.get_text())
        if self.is_valid_password(password):
            self.n = Network(server, port)
            self.run = True
            print(server)
            print(port)
            try:
                self.n.send(pickle.dumps(ProcessData("get_adm", [0], 0)))
                label_adm_info.set_text(f"Administrator connected to: {server}_{port}")
                label_adm_info.css_visibility = "visible"
            except Exception as e:
                self.run = False
            self._disable_button(widget)
            self._enable_button(button_adm_disconnect)
            textEditPassAdm.set_text("")
            self._enable_button(button_adm_setperiod)
        else:
            pass
            # self.logger.error("Invalid password")

    def is_valid_password(self, password):
        return password == "1"

    def _enable_button(self, button):
        button.set_enabled(True)
        button.css_background_color = ENABLED_COLOR

    def _disable_button(self, button):
        button.set_enabled(False)
        button.css_background_color = DISABLED_COLOR

    def on_button_adm_disconnect_pressed(self, button_adm_connect, widget):
        self.n.send(pickle.dumps(ProcessData("disconnect", [0], 0)))
        self._enable_button(button_adm_connect)
        self._disable_button(widget)

    def on_button_adm_set_period_pressed(self, textEditSetPeriod, label_adm_turnstatus, textEditSetCustDemand,
                                         button_adm_update, widget):
        new_period = int(textEditSetPeriod.get_text())
        if int(self.adm_period) < new_period:
            self.adm_period = new_period
            self.current_period = new_period
            label_adm_turnstatus.text = f"{self.current_period} Turn Status"
            self.n.send(pickle.dumps(ProcessData("set_period", [0], self.adm_period)))
            adm_demand = textEditSetCustDemand.get_text()
            self.n.send(pickle.dumps(ProcessData("set_demand", [0], adm_demand)))
            self._enable_button(button_adm_update)
        else:
            pass

    def on_button_adm_update_pressed(self, label_adm_status, widget):
        status_text = self.n.send(pickle.dumps(ProcessData("check_status", [0], 0)))
        label_adm_status.text = status_text


# Configuration
configuration = {'config_project_name': 'adm_remi', 'config_address': '0.0.0.0', 'config_port': 8084,
                 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True,
                 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(adm_remi, address=configuration['config_address'], port=configuration['config_port'],
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
