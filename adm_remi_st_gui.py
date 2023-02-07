from remi.gui import *
import adm_remi_st
import functools

DISABLED_COLOR = "rgb(200,200,200)"
ENABLED_COLOR = "rgb(100,100,100)"


# @staticmethod
def construct_ui(self):
    # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
    container0 = Container()
    container0.attr_class = "Container"
    container0.attr_editor_newclass = False
    container0.css_align_self = "center"
    container0.css_background_color = "rgb(230,230,230)"
    container0.css_height = "600px"
    container0.css_left = "20.0px"
    container0.css_position = "absolute"
    container0.css_top = "20.0px"
    container0.css_width = "800px"
    container0.variable_name = "container0"
    label_adm_setperiod = Label()
    label_adm_setperiod.attr_class = "Label"
    label_adm_setperiod.attr_editor_newclass = False
    label_adm_setperiod.css_font_family = "Tahoma"
    label_adm_setperiod.css_font_size = "18px"
    label_adm_setperiod.css_height = "30px"
    label_adm_setperiod.css_left = "10.0px"
    label_adm_setperiod.css_position = "absolute"
    label_adm_setperiod.css_top = "60.0px"
    label_adm_setperiod.css_width = "100px"
    label_adm_setperiod.text = "Period: "
    label_adm_setperiod.variable_name = "label_adm_setperiod"
    container0.append(label_adm_setperiod, 'label_adm_setperiod')
    label_adm_period = Label()
    label_adm_period.attr_class = "Label"
    label_adm_period.attr_editor_newclass = False
    label_adm_period.css_font_family = "Tahoma"
    label_adm_period.css_font_size = "22px"
    label_adm_period.css_font_style = "normal"
    label_adm_period.css_font_weight = "bold"
    label_adm_period.css_height = "30.0px"
    label_adm_period.css_left = "10.0px"
    label_adm_period.css_position = "absolute"
    label_adm_period.css_top = "10.0px"
    label_adm_period.css_width = "180.0px"
    label_adm_period.text = "Current Period:"
    label_adm_period.variable_name = "label_adm_period"
    container0.append(label_adm_period, 'label_adm_period')
    label_adm_setcustdemand = Label()
    label_adm_setcustdemand.attr_class = "Label"
    label_adm_setcustdemand.attr_editor_newclass = False
    label_adm_setcustdemand.css_font_family = "Tahoma"
    label_adm_setcustdemand.css_font_size = "18px"
    label_adm_setcustdemand.css_height = "30px"
    label_adm_setcustdemand.css_left = "10.0px"
    label_adm_setcustdemand.css_position = "absolute"
    label_adm_setcustdemand.css_top = "110.0px"
    label_adm_setcustdemand.css_width = "100px"
    label_adm_setcustdemand.text = "Demand:"
    label_adm_setcustdemand.variable_name = "label_adm_setcustdemand"
    container0.append(label_adm_setcustdemand, 'label_adm_setcustdemand')
    self.textEditSetPeriod = TextInput()
    self.textEditSetPeriod.attr_class = "TextInput"
    self.textEditSetPeriod.attr_editor_newclass = False
    self.textEditSetPeriod.css_font_family = "tahoma"
    self.textEditSetPeriod.css_font_size = "20px"
    self.textEditSetPeriod.css_height = "30.0px"
    self.textEditSetPeriod.css_left = "110.0px"
    self.textEditSetPeriod.css_position = "absolute"
    self.textEditSetPeriod.css_top = "60.0px"
    self.textEditSetPeriod.css_width = "75.0px"
    self.textEditSetPeriod.text = "1"
    self.textEditSetPeriod.css_text_align = "right"
    self.textEditSetPeriod.variable_name = "textEditSetPeriod"
    container0.append(self.textEditSetPeriod, 'textEditSetPeriod')
    self.textEditSetCustDemand = TextInput()
    self.textEditSetCustDemand.attr_class = "TextInput"
    self.textEditSetCustDemand.attr_editor_newclass = False
    self.textEditSetCustDemand.css_font_family = "tahoma"
    self.textEditSetCustDemand.css_font_size = "20px"
    self.textEditSetCustDemand.css_height = "30.0px"
    self.textEditSetCustDemand.css_left = "110.0px"
    self.textEditSetCustDemand.css_position = "absolute"
    self.textEditSetCustDemand.css_top = "110.0px"
    self.textEditSetCustDemand.css_width = "75.0px"
    self.textEditSetCustDemand.text = "5"
    self.textEditSetCustDemand.css_text_align = "right"
    self.textEditSetCustDemand.variable_name = "textEditSetCustDemand"
    container0.append(self.textEditSetCustDemand, 'textEditSetCustDemand')
    self.button_adm_setperiod = Button()
    self.button_adm_setperiod.attr_class = "Button"
    self.button_adm_setperiod.attr_editor_newclass = False
    self.button_adm_setperiod.css_border_style = "none"
    self.button_adm_setperiod.css_flex = "1"
    self.button_adm_setperiod.css_font_family = "Tahoma"
    self.button_adm_setperiod.css_font_size = "16px"
    self.button_adm_setperiod.css_height = "85.0px"
    self.button_adm_setperiod.css_left = "200.0px"
    self.button_adm_setperiod.css_position = "absolute"
    self.button_adm_setperiod.css_top = "60.0px"
    self.button_adm_setperiod.css_width = "100.0px"
    self.button_adm_setperiod.text = "Set period and demand"
    self.button_adm_setperiod.variable_name = "button_adm_setperiod"
    self.button_adm_setperiod.css_background_color = "rgb(100,100,100)"
    self.button_adm_setperiod.css_color = "rgb(255,255,255)"
    container0.append(self.button_adm_setperiod, 'button_adm_setperiod')
    self.label_adm_info = Label()
    self.label_adm_info.attr_class = "Label"
    self.label_adm_info.attr_editor_newclass = False
    self.label_adm_info.css_height = "30.0px"
    self.label_adm_info.css_left = "10.0px"
    self.label_adm_info.css_position = "absolute"
    self.label_adm_info.css_top = "555.0px"
    self.label_adm_info.css_width = "300.0px"
    self.label_adm_info.text = "Info"
    self.label_adm_info.variable_name = "label_adm_info"
    self.label_adm_info.css_font_family = "tahoma"
    self.label_adm_info.css_font_size = "12px"
    container0.append(self.label_adm_info, 'label_adm_info')
    label_adm_pass = Label()
    label_adm_pass.attr_class = "Label"
    label_adm_pass.attr_editor_newclass = False
    label_adm_pass.css_height = "30.0px"
    label_adm_pass.css_left = "10.0px"
    label_adm_pass.css_position = "absolute"
    label_adm_pass.css_top = "425.0px"
    label_adm_pass.css_width = "60.0px"
    label_adm_pass.text = "Password:"
    label_adm_pass.css_font_family = "Tahoma"
    label_adm_pass.variable_name = "label_adm_pass"
    container0.append(label_adm_pass, 'label_adm_pass')
    label_adm_server = Label()
    label_adm_server.attr_class = "Label"
    label_adm_server.attr_editor_newclass = False
    label_adm_server.css_height = "30.0px"
    label_adm_server.css_left = "10.0px"
    label_adm_server.css_position = "absolute"
    label_adm_server.css_top = "465.0px"
    label_adm_server.css_width = "60.0px"
    label_adm_server.text = "Server:"
    label_adm_server.css_font_family = "Tahoma"
    label_adm_server.variable_name = "label_adm_server"
    container0.append(label_adm_server, 'label_adm_server')
    label_adm_port = Label()
    label_adm_port.attr_class = "Label"
    label_adm_port.attr_editor_newclass = False
    label_adm_port.css_height = "30.0px"
    label_adm_port.css_left = "10.0px"
    label_adm_port.css_position = "absolute"
    label_adm_port.css_top = "510.0px"
    label_adm_port.css_width = "45.0px"
    label_adm_port.text = "Port:"
    label_adm_port.css_font_family = "Tahoma"
    label_adm_port.variable_name = "label_adm_port"
    container0.append(label_adm_port, 'label_adm_port')
    self.textEditServerAdm = TextInput()
    self.textEditServerAdm.attr_class = "TextInput"
    self.textEditServerAdm.attr_editor_newclass = False
    self.textEditServerAdm.css_font_family = "Tahoma"
    self.textEditServerAdm.css_height = "30.0px"
    self.textEditServerAdm.css_left = "75.0px"
    self.textEditServerAdm.css_position = "absolute"
    self.textEditServerAdm.css_top = "465.0px"
    self.textEditServerAdm.css_width = "225.0px"
    self.textEditServerAdm.text = "localhost"
    self.textEditServerAdm.css_text_align = "center"
    self.textEditServerAdm.variable_name = "textEditServerAdm"
    container0.append(self.textEditServerAdm, 'textEditServerAdm')
    self.textEditPassAdm = TextInput()
    self.textEditPassAdm.attr_class = "TextInput"
    self.textEditPassAdm.attr_editor_newclass = False
    self.textEditPassAdm.css_font_family = "Tahoma"
    self.textEditPassAdm.css_height = "30.0px"
    self.textEditPassAdm.css_left = "75.0px"
    self.textEditPassAdm.css_position = "absolute"
    self.textEditPassAdm.css_top = "425.0px"
    self.textEditPassAdm.css_width = "225.0px"
    self.textEditPassAdm.text = "passphrase"
    self.textEditPassAdm.css_text_align = "center"
    self.textEditPassAdm.variable_name = "textEditPassAdm"
    container0.append(self.textEditPassAdm, 'textEditPassAdm')
    self.textEditPortAdm = TextInput()
    self.textEditPortAdm.attr_class = "TextInput"
    self.textEditPortAdm.attr_editor_newclass = False
    self.textEditPortAdm.css_align_self = "center"
    self.textEditPortAdm.css_font_family = "Tahoma"
    self.textEditPortAdm.css_height = "40.0px"
    self.textEditPortAdm.css_left = "75.0px"
    self.textEditPortAdm.css_position = "absolute"
    self.textEditPortAdm.css_top = "510.0px"
    self.textEditPortAdm.css_width = "120.0px"
    self.textEditPortAdm.text = "5555"
    self.textEditPortAdm.css_text_align = "center"
    self.textEditPortAdm.variable_name = "textEditPortAdm"
    container0.append(self.textEditPortAdm, 'textEditPortAdm')
    self.button_adm_connect = Button()
    self.button_adm_connect.attr_class = "Button"
    self.button_adm_connect.css_border_style = "none"
    self.button_adm_connect.attr_editor_newclass = False
    self.button_adm_connect.css_font_family = "Tahoma"
    self.button_adm_connect.css_font_size = "16px"
    self.button_adm_connect.css_height = "45.0px"
    self.button_adm_connect.css_left = "210.0px"
    self.button_adm_connect.css_position = "absolute"
    self.button_adm_connect.css_top = "510.0px"
    self.button_adm_connect.css_width = "90.0px"
    self.button_adm_connect.text = "Connect"
    self.button_adm_connect.variable_name = "button_adm_connect"
    self.button_adm_connect.css_background_color = "rgb(100,100,100)"
    self.button_adm_connect.css_color = "rgb(255,255,255)"
    container0.append(self.button_adm_connect, 'button_adm_connect')
    self.button_adm_disconnect = Button()
    self.button_adm_disconnect.attr_class = "Button"
    self.button_adm_disconnect.css_border_style = "none"
    self.button_adm_disconnect.attr_editor_newclass = False
    self.button_adm_disconnect.css_font_family = "Tahoma"
    self.button_adm_disconnect.css_font_size = "16px"
    self.button_adm_disconnect.css_height = "45.0px"
    self.button_adm_disconnect.css_left = "690.0px"
    self.button_adm_disconnect.css_position = "absolute"
    self.button_adm_disconnect.css_top = "10.0px"
    self.button_adm_disconnect.css_width = "90.0px"
    self.button_adm_disconnect.text = "Disconnect"
    self.button_adm_disconnect.variable_name = "button_adm_disconnect"
    self.button_adm_disconnect.css_background_color = "rgb(100,100,100)"
    self.button_adm_disconnect.css_color = "rgb(255,255,255)"
    container0.append(self.button_adm_disconnect, 'button_adm_disconnect')
    self.button_adm_update = Button()
    self.button_adm_update.attr_class = "Button"
    self.button_adm_update.css_border_style = "none"
    self.button_adm_update.attr_editor_newclass = False
    self.button_adm_update.css_font_family = "Tahoma"
    self.button_adm_update.css_font_size = "16px"
    self.button_adm_update.css_height = "40.0px"
    self.button_adm_update.css_left = "690.0px"
    self.button_adm_update.css_position = "absolute"
    self.button_adm_update.css_top = "510.0px"
    self.button_adm_update.css_width = "100.0px"
    self.button_adm_update.text = "Update all"
    self.button_adm_update.variable_name = "button_adm_update"
    self.button_adm_update.css_background_color = "rgb(100,100,100)"
    self.button_adm_update.css_color = "rgb(255,255,255)"
    container0.append(self.button_adm_update, 'button_adm_update')
    self.label_adm_turnstatus = Label()
    self.label_adm_turnstatus.attr_class = "Label"
    self.label_adm_turnstatus.attr_editor_newclass = False
    self.label_adm_turnstatus.css_font_family = "Tahoma"
    self.label_adm_turnstatus.css_font_size = "22px"
    self.label_adm_turnstatus.css_font_weight = "bold"
    self.label_adm_turnstatus.css_height = "40.0px"
    self.label_adm_turnstatus.css_left = "520.0px"
    self.label_adm_turnstatus.css_position = "absolute"
    self.label_adm_turnstatus.css_top = "10.0px"
    self.label_adm_turnstatus.css_width = "180.0px"
    self.label_adm_turnstatus.text = "Turn Status:"
    self.label_adm_turnstatus.variable_name = "label_adm_turnstatus"
    container0.append(self.label_adm_turnstatus, 'label_adm_turnstatus')
    label_adm_leadtime = Label()
    label_adm_leadtime.attr_class = "Label"
    label_adm_leadtime.attr_editor_newclass = False
    label_adm_leadtime.css_font_family = "tahoma"
    label_adm_leadtime.css_font_size = "14px"
    label_adm_leadtime.css_font_weight = "bold"
    label_adm_leadtime.css_height = "30.0px"
    label_adm_leadtime.css_left = "320.0px"
    label_adm_leadtime.css_position = "absolute"
    label_adm_leadtime.css_top = "50.0px"
    label_adm_leadtime.css_width = "190.0px"
    label_adm_leadtime.text = "Lead Time Distributor:"
    label_adm_leadtime.variable_name = "label_adm_leadtime"
    container0.append(label_adm_leadtime, 'label_adm_leadtime')
    self.label_adm_status = Label()
    self.label_adm_status.attr_class = "Label"
    self.label_adm_status.attr_editor_newclass = False
    self.label_adm_status.css_font_family = "tahoma"
    self.label_adm_status.css_font_size = "14px"
    self.label_adm_status.css_height = "260.0px"
    self.label_adm_status.css_left = "520.0px"
    self.label_adm_status.css_position = "absolute"
    self.label_adm_status.css_top = "50.0px"
    self.label_adm_status.css_width = "270.0px"
    self.label_adm_status.text = "Turn status info"
    self.label_adm_status.css_white_space = "pre-wrap"
    self.label_adm_status.variable_name = "label_adm_status"
    container0.append(self.label_adm_status, 'label_adm_status')
    label_adm_intransit = Label()
    label_adm_intransit.attr_class = "Label"
    label_adm_intransit.attr_editor_newclass = False
    label_adm_intransit.css_font_family = "tahoma"
    label_adm_intransit.css_font_size = "14px"
    label_adm_intransit.css_font_weight = "bold"
    label_adm_intransit.css_height = "30.0px"
    label_adm_intransit.css_left = "320.0px"
    label_adm_intransit.css_position = "absolute"
    label_adm_intransit.css_top = "10.0px"
    label_adm_intransit.css_width = "130.0px"
    label_adm_intransit.text = "In transit:"
    label_adm_intransit.variable_name = "label_adm_intransit"
    label_adm_intransit.css_visibility = "hidden"
    container0.append(label_adm_intransit, 'label_adm_intransit')
    label_adm_backlog = Label()
    label_adm_backlog.attr_class = "Label"
    label_adm_backlog.attr_editor_newclass = False
    label_adm_backlog.css_font_family = "tahoma"
    label_adm_backlog.css_font_size = "14px"
    label_adm_backlog.css_font_weight = "bold"
    label_adm_backlog.css_height = "30.0px"
    label_adm_backlog.css_left = "320.0px"
    label_adm_backlog.css_position = "absolute"
    label_adm_backlog.css_top = "90.0px"
    label_adm_backlog.css_width = "190.0px"
    label_adm_backlog.text = "Backlog:"
    label_adm_backlog.variable_name = "label_adm_backlog"
    container0.append(label_adm_backlog, 'label_adm_backlog')
    label_adm_inventory = Label()
    label_adm_inventory.attr_class = "Label"
    label_adm_inventory.attr_editor_newclass = False
    label_adm_inventory.css_font_family = "tahoma"
    label_adm_inventory.css_font_size = "14px"
    label_adm_inventory.css_font_weight = "bold"
    label_adm_inventory.css_height = "30.0px"
    label_adm_inventory.css_left = "320.0px"
    label_adm_inventory.css_position = "absolute"
    label_adm_inventory.css_top = "130.0px"
    label_adm_inventory.css_width = "190.0px"
    label_adm_inventory.text = "Inventory:"
    label_adm_inventory.variable_name = "label_adm_inventory"
    container0.append(label_adm_inventory, 'label_adm_inventory')
    label_adm_demand = Label()
    label_adm_demand.attr_class = "Label"
    label_adm_demand.attr_editor_newclass = False
    label_adm_demand.css_font_family = "tahoma"
    label_adm_demand.css_font_size = "14px"
    label_adm_demand.css_font_weight = "bold"
    label_adm_demand.css_height = "30.0px"
    label_adm_demand.css_left = "320.0px"
    label_adm_demand.css_position = "absolute"
    label_adm_demand.css_top = "170.0px"
    label_adm_demand.css_width = "200.0px"
    label_adm_demand.text = "Demand:"
    label_adm_demand.variable_name = "label_adm_demand"
    container0.append(label_adm_demand, 'label_adm_demand')

    self.button_adm_setperiod.set_enabled(False)
    self.button_adm_update.set_enabled(False)
    self.button_adm_setperiod.css_background_color = "rgb(200,200,200)"
    self.button_adm_update.css_background_color = "rgb(200,200,200)"
    self.button_adm_disconnect.set_enabled(False)
    self.button_adm_disconnect.css_background_color = "rgb(200,200,200)"
    self.label_adm_info.set_text("Info")
    # label_adm_info.css_visibility = "invisible"

    self.button_adm_connect.onclick.do(functools.partial(self.on_button_adm_connect_pressed,
                                                         self.textEditPassAdm, self.textEditServerAdm,
                                                         self.textEditPortAdm, self.label_adm_info,
                                                         self.button_adm_disconnect, self.button_adm_setperiod))
    self.button_adm_setperiod.onclick.do(functools.partial(self.on_button_adm_set_period_pressed,
                                                           self.textEditSetPeriod, self.label_adm_turnstatus,
                                                           self.textEditSetCustDemand, self.button_adm_update))
    self.button_adm_update.onclick.do(functools.partial(self.on_button_adm_update_pressed, self.label_adm_status))
    self.button_adm_disconnect.onclick.do(functools.partial(self.on_button_adm_disconnect_pressed,
                                                            self.button_adm_connect))

    return container0


def on_button_adm_connect_pressed(self, widget):
    widgets = [self.textEditPassAdm, self.textEditServerAdm, self.textEditPortAdm, self.label_adm_info,
               self.button_adm_disconnect, self.button_adm_setperiod]
    adm_remi_st.adm_remi.on_button_adm_connect_pressed(functools.partial(self, *widgets))


def on_button_adm_disconnect_pressed(self, widget):
    adm_remi_st.adm_remi.on_button_adm_disconnect_pressed(functools.partial(self, self.button_adm_connect))


def on_button_adm_set_period_pressed(self, widget):
    widgets = [self.textEditSetPeriod, self.label_adm_turnstatus, self.textEditSetCustDemand, self.button_adm_update]
    adm_remi_st.adm_remi.on_button_adm_set_period_pressed(functools.partial(self, *widgets))


def on_button_adm_update_pressed(self, widget):
    adm_remi_st.adm_remi.on_button_adm_update_pressed(functools.partial(self, self.label_adm_status))
