from remi.gui import *
import distr_remi_st
import functools


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
    label_distr_ordersize = Label()
    label_distr_ordersize.attr_class = "Label"
    label_distr_ordersize.attr_editor_newclass = False
    label_distr_ordersize.css_font_family = "Tahoma"
    label_distr_ordersize.css_font_size = "18px"
    label_distr_ordersize.css_height = "30px"
    label_distr_ordersize.css_left = "10.0px"
    label_distr_ordersize.css_position = "absolute"
    label_distr_ordersize.css_top = "55.0px"
    label_distr_ordersize.css_width = "100px"
    label_distr_ordersize.text = "Order Size:"
    label_distr_ordersize.variable_name = "label_distr_ordersize"
    container0.append(label_distr_ordersize, 'label_distr_ordersize')
    label_distr_shipment = Label()
    label_distr_shipment.attr_class = "Label"
    label_distr_shipment.attr_editor_newclass = False
    label_distr_shipment.css_font_family = "Tahoma"
    label_distr_shipment.css_font_size = "18px"
    label_distr_shipment.css_height = "30px"
    label_distr_shipment.css_left = "10.0px"
    label_distr_shipment.css_position = "absolute"
    label_distr_shipment.css_top = "95.0px"
    label_distr_shipment.css_width = "100px"
    label_distr_shipment.text = "Shipment:"
    label_distr_shipment.variable_name = "label_distr_shipment"
    container0.append(label_distr_shipment, 'label_distr_shipment')
    self.label_distr_period = Label()
    self.label_distr_period.attr_class = "Label"
    self.label_distr_period.attr_editor_newclass = False
    self.label_distr_period.css_font_family = "Tahoma"
    self.label_distr_period.css_font_size = "22px"
    self.label_distr_period.css_font_style = "normal"
    self.label_distr_period.css_font_weight = "bold"
    self.label_distr_period.css_height = "30.0px"
    self.label_distr_period.css_left = "10.0px"
    self.label_distr_period.css_position = "absolute"
    self.label_distr_period.css_top = "10.0px"
    self.label_distr_period.css_width = "280.0px"
    self.label_distr_period.text = "Current Period: 0"
    self.label_distr_period.variable_name = "label_distr_period"
    container0.append(self.label_distr_period, 'label_distr_period')
    self.textEditOrderDistributor = TextInput()
    self.textEditOrderDistributor.attr_class = "TextInput"
    self.textEditOrderDistributor.attr_editor_newclass = False
    self.textEditOrderDistributor.css_font_family = "tahoma"
    self.textEditOrderDistributor.css_font_size = "20px"
    self.textEditOrderDistributor.css_height = "30.0px"
    self.textEditOrderDistributor.css_left = "110.0px"
    self.textEditOrderDistributor.css_position = "absolute"
    self.textEditOrderDistributor.css_text_align = "right"
    self.textEditOrderDistributor.css_top = "60.0px"
    self.textEditOrderDistributor.css_width = "75.0px"
    self.textEditOrderDistributor.text = "1"
    self.textEditOrderDistributor.variable_name = "textEditOrderDistributor"
    container0.append(self.textEditOrderDistributor, 'textEditOrderDistributor')
    self.textEditShipmentDistributor = TextInput()
    self.textEditShipmentDistributor.attr_class = "TextInput"
    self.textEditShipmentDistributor.attr_editor_newclass = False
    self.textEditShipmentDistributor.css_font_family = "tahoma"
    self.textEditShipmentDistributor.css_font_size = "20px"
    self.textEditShipmentDistributor.css_height = "30.0px"
    self.textEditShipmentDistributor.css_left = "110.0px"
    self.textEditShipmentDistributor.css_position = "absolute"
    self.textEditShipmentDistributor.css_text_align = "right"
    self.textEditShipmentDistributor.css_top = "100.0px"
    self.textEditShipmentDistributor.css_width = "75.0px"
    self.textEditShipmentDistributor.text = "1"
    self.textEditShipmentDistributor.variable_name = "textEditShipmentDistributor"
    container0.append(self.textEditShipmentDistributor, 'textEditShipmentDistributor')
    self.label_distr_info = Label()
    self.label_distr_info.attr_class = "Label"
    self.label_distr_info.attr_editor_newclass = False
    self.label_distr_info.css_height = "30.0px"
    self.label_distr_info.css_left = "10.0px"
    self.label_distr_info.css_position = "absolute"
    self.label_distr_info.css_top = "555.0px"
    self.label_distr_info.text = "Info"
    self.label_distr_info.css_visibility = "hidden"
    self.label_distr_info.variable_name = "label_distr_info"
    self.label_distr_info.css_width = "300.0px"
    self.label_distr_info.css_font_family = "tahoma"
    self.label_distr_info.css_font_size = "12px"
    container0.append(self.label_distr_info, 'label_distr_info')
    label_distr_server = Label()
    label_distr_server.attr_class = "Label"
    label_distr_server.attr_editor_newclass = False
    label_distr_server.css_height = "30.0px"
    label_distr_server.css_left = "10.0px"
    label_distr_server.css_position = "absolute"
    label_distr_server.css_top = "465.0px"
    label_distr_server.css_width = "60.0px"
    label_distr_server.text = "Server:"
    label_distr_server.variable_name = "label_distr_server"
    label_distr_server.css_font_family = "Tahoma"
    container0.append(label_distr_server, 'label_distr_server')
    label_distr_pass = Label()
    label_distr_pass.attr_class = "Label"
    label_distr_pass.attr_editor_newclass = False
    label_distr_pass.css_height = "30.0px"
    label_distr_pass.css_left = "10.0px"
    label_distr_pass.css_position = "absolute"
    label_distr_pass.css_top = "425.0px"
    label_distr_pass.css_width = "60.0px"
    label_distr_pass.text = "Password:"
    label_distr_pass.css_font_family = "Tahoma"
    label_distr_pass.css_font_size = "14px"
    label_distr_pass.variable_name = "label_distr_pass"
    container0.append(label_distr_pass, 'label_distr_pass')
    label_distr_port = Label()
    label_distr_port.attr_class = "Label"
    label_distr_port.attr_editor_newclass = False
    label_distr_port.css_height = "30.0px"
    label_distr_port.css_left = "10.0px"
    label_distr_port.css_position = "absolute"
    label_distr_port.css_top = "510.0px"
    label_distr_port.css_width = "45.0px"
    label_distr_port.text = "Port:"
    label_distr_port.variable_name = "label_distr_port"
    container0.append(label_distr_port, 'label_distr_port')
    self.textEditServerDistr = TextInput()
    self.textEditServerDistr.attr_class = "TextInput"
    self.textEditServerDistr.attr_editor_newclass = False
    self.textEditServerDistr.css_font_family = "Tahoma"
    self.textEditServerDistr.css_height = "30.0px"
    self.textEditServerDistr.css_left = "75.0px"
    self.textEditServerDistr.css_position = "absolute"
    self.textEditServerDistr.css_text_align = "center"
    self.textEditServerDistr.css_top = "465.0px"
    self.textEditServerDistr.css_width = "225.0px"
    self.textEditServerDistr.text = "localhost"
    self.textEditServerDistr.variable_name = "textEditServerDistr"
    container0.append(self.textEditServerDistr, 'textEditServerDistr')
    self.textEditPassDistr = TextInput()
    self.textEditPassDistr.attr_class = "TextInput"
    self.textEditPassDistr.attr_editor_newclass = False
    self.textEditPassDistr.css_font_family = "Tahoma"
    self.textEditPassDistr.css_height = "30.0px"
    self.textEditPassDistr.css_left = "75.0px"
    self.textEditPassDistr.css_position = "absolute"
    self.textEditPassDistr.css_top = "425.0px"
    self.textEditPassDistr.css_width = "225.0px"
    self.textEditPassDistr.text = "passphrase"
    self.textEditPassDistr.css_text_align = "center"
    self.textEditPassDistr.variable_name = "textEditPassDistr"
    container0.append(self.textEditPassDistr, 'textEditPassDistr')
    self.textEditPortDistr = TextInput()
    self.textEditPortDistr.attr_class = "TextInput"
    self.textEditPortDistr.attr_editor_newclass = False
    self.textEditPortDistr.css_align_self = "center"
    self.textEditPortDistr.css_font_family = "Tahoma"
    self.textEditPortDistr.css_height = "40.0px"
    self.textEditPortDistr.css_left = "75.0px"
    self.textEditPortDistr.css_position = "absolute"
    self.textEditPortDistr.css_text_align = "center"
    self.textEditPortDistr.css_top = "510.0px"
    self.textEditPortDistr.css_width = "120.0px"
    self.textEditPortDistr.text = "5555"
    self.textEditPortDistr.variable_name = "textEditPortDistr"
    container0.append(self.textEditPortDistr, 'textEditPortDistr')
    self.button_distr_connect = Button()
    self.button_distr_connect.attr_class = "Button"
    self.button_distr_connect.css_border_style = "none"
    self.button_distr_connect.attr_editor_newclass = False
    self.button_distr_connect.css_background_color = "rgb(158,176,253)"
    self.button_distr_connect.css_font_family = "Tahoma"
    self.button_distr_connect.css_font_size = "16px"
    self.button_distr_connect.css_height = "40.0px"
    self.button_distr_connect.css_left = "210.0px"
    self.button_distr_connect.css_position = "absolute"
    self.button_distr_connect.css_top = "510.0px"
    self.button_distr_connect.css_width = "90.0px"
    self.button_distr_connect.text = "Connect"
    self.button_distr_connect.css_color = "rgb(255,255,255)"
    self.button_distr_connect.variable_name = "button_distr_connect"
    container0.append(self.button_distr_connect, 'button_distr_connect')
    self.button_distr_disconnect = Button()
    self.button_distr_disconnect.attr_class = "Button"
    self.button_distr_disconnect.css_border_style = "none"
    self.button_distr_disconnect.attr_editor_newclass = False
    self.button_distr_disconnect.css_background_color = "rgb(158,176,253)"
    self.button_distr_disconnect.css_font_family = "Tahoma"
    self.button_distr_disconnect.css_font_size = "16px"
    self.button_distr_disconnect.css_height = "40.0px"
    self.button_distr_disconnect.css_left = "690.0px"
    self.button_distr_disconnect.css_position = "absolute"
    self.button_distr_disconnect.css_top = "10.0px"
    self.button_distr_disconnect.css_width = "100.0px"
    self.button_distr_disconnect.text = "Disconnect"
    self.button_distr_disconnect.css_color = "rgb(255,255,255)"
    self.button_distr_disconnect.variable_name = "button_distr_disconnect"
    container0.append(self.button_distr_disconnect, 'button_distr_disconnect')
    self.button_distr_update = Button()
    self.button_distr_update.attr_class = "Button"
    self.button_distr_update.css_border_style = "none"
    self.button_distr_update.attr_editor_newclass = False
    self.button_distr_update.css_background_color = "rgb(158,176,253)"
    self.button_distr_update.css_font_family = "Tahoma"
    self.button_distr_update.css_font_size = "16px"
    self.button_distr_update.css_height = "40.0px"
    self.button_distr_update.css_left = "690.0px"
    self.button_distr_update.css_position = "absolute"
    self.button_distr_update.css_top = "510.0px"
    self.button_distr_update.css_width = "100.0px"
    self.button_distr_update.text = "Update"
    self.button_distr_update.css_color = "rgb(255,255,255)"
    self.button_distr_update.variable_name = "button_distr_update"
    container0.append(self.button_distr_update, 'button_distr_update')
    label_distr_turnstatus = Label()
    label_distr_turnstatus.attr_class = "Label"
    label_distr_turnstatus.attr_editor_newclass = False
    label_distr_turnstatus.css_font_family = "Tahoma"
    label_distr_turnstatus.css_font_size = "22px"
    label_distr_turnstatus.css_font_weight = "bold"
    label_distr_turnstatus.css_height = "40.0px"
    label_distr_turnstatus.css_left = "520.0px"
    label_distr_turnstatus.css_position = "absolute"
    label_distr_turnstatus.css_top = "10.0px"
    label_distr_turnstatus.css_width = "160.0px"
    label_distr_turnstatus.text = "Turn Status"
    label_distr_turnstatus.variable_name = "label_distr_turnstatus"
    container0.append(label_distr_turnstatus, 'label_distr_turnstatus')
    label_distr_leadtime = Label()
    label_distr_leadtime.attr_class = "Label"
    label_distr_leadtime.attr_editor_newclass = False
    label_distr_leadtime.css_font_family = "tahoma"
    label_distr_leadtime.css_font_size = "14px"
    label_distr_leadtime.css_font_weight = "bold"
    label_distr_leadtime.css_height = "30.0px"
    label_distr_leadtime.css_left = "320.0px"
    label_distr_leadtime.css_position = "absolute"
    label_distr_leadtime.css_top = "50.0px"
    label_distr_leadtime.css_width = "190.0px"
    label_distr_leadtime.set_text("Leadtime to Wholesaler: " + str(distr_remi_st.LEADTIMEUP))
    label_distr_leadtime.variable_name = "label_distr_leadtime"
    container0.append(label_distr_leadtime, 'label_distr_leadtime')
    self.label_distr_status = Label()
    self.label_distr_status.attr_class = "Label"
    self.label_distr_status.attr_editor_newclass = False
    self.label_distr_status.css_font_family = "tahoma"
    self.label_distr_status.css_font_size = "14px"
    self.label_distr_status.css_height = "260.0px"
    self.label_distr_status.css_left = "520.0px"
    self.label_distr_status.css_position = "absolute"
    self.label_distr_status.css_top = "50.0px"
    self.label_distr_status.css_white_space = "pre-wrap"
    self.label_distr_status.css_width = "270.0px"
    self.label_distr_status.text = "Turn status info"
    self.label_distr_status.variable_name = "label_distr_status"
    container0.append(self.label_distr_status, 'label_distr_status')
    label_distr_intransit = Label()
    label_distr_intransit.attr_class = "Label"
    label_distr_intransit.attr_editor_newclass = False
    label_distr_intransit.css_font_family = "tahoma"
    label_distr_intransit.css_font_size = "14px"
    label_distr_intransit.css_font_weight = "bold"
    label_distr_intransit.css_height = "30.0px"
    label_distr_intransit.css_left = "320.0px"
    label_distr_intransit.css_position = "absolute"
    label_distr_intransit.css_top = "10.0px"
    label_distr_intransit.css_width = "130.0px"
    label_distr_intransit.text = "In transit:"
    label_distr_intransit.variable_name = "label_distr_intransit"
    label_distr_intransit.css_visibility = "hidden"
    container0.append(label_distr_intransit, 'label_distr_intransit')
    self.label_distr_backlog = Label()
    self.label_distr_backlog.attr_class = "Label"
    self.label_distr_backlog.attr_editor_newclass = False
    self.label_distr_backlog.css_font_family = "tahoma"
    self.label_distr_backlog.css_font_size = "14px"
    self.label_distr_backlog.css_font_weight = "bold"
    self.label_distr_backlog.css_height = "30.0px"
    self.label_distr_backlog.css_left = "320.0px"
    self.label_distr_backlog.css_position = "absolute"
    self.label_distr_backlog.css_top = "90.0px"
    self.label_distr_backlog.css_width = "190.0px"
    self.label_distr_backlog.text = "Backlog (total):"
    self.label_distr_backlog.variable_name = "label_distr_backlog"
    container0.append(self.label_distr_backlog, 'label_distr_backlog')
    self.label_distr_inventory = Label()
    self.label_distr_inventory.attr_class = "Label"
    self.label_distr_inventory.attr_editor_newclass = False
    self.label_distr_inventory.css_font_family = "tahoma"
    self.label_distr_inventory.css_font_size = "14px"
    self.label_distr_inventory.css_font_weight = "bold"
    self.label_distr_inventory.css_height = "30.0px"
    self.label_distr_inventory.css_left = "320.0px"
    self.label_distr_inventory.css_position = "absolute"
    self.label_distr_inventory.css_top = "130.0px"
    self.label_distr_inventory.css_width = "190.0px"
    self.label_distr_inventory.text = "Inventory:"
    self.label_distr_inventory.variable_name = "label_distr_inventory"
    container0.append(self.label_distr_inventory, 'label_distr_inventory')
    self.label_distr_demand = Label()
    self.label_distr_demand.attr_class = "Label"
    self.label_distr_demand.attr_editor_newclass = False
    self.label_distr_demand.css_font_family = "tahoma"
    self.label_distr_demand.css_font_size = "14px"
    self.label_distr_demand.css_font_weight = "bold"
    self.label_distr_demand.css_height = "30.0px"
    self.label_distr_demand.css_left = "320.0px"
    self.label_distr_demand.css_position = "absolute"
    self.label_distr_demand.css_top = "170.0px"
    self.label_distr_demand.css_width = "190.0px"
    self.label_distr_demand.text = "Demand:"
    self.label_distr_demand.variable_name = "label_distr_demand"
    container0.append(self.label_distr_demand, 'label_distr_demand')
    self.label_distr_costs = Label()
    self.label_distr_costs.attr_class = "Label"
    self.label_distr_costs.attr_editor_newclass = False
    self.label_distr_costs.css_font_family = "tahoma"
    self.label_distr_costs.css_font_size = "18px"
    self.label_distr_costs.css_height = "30.0px"
    self.label_distr_costs.css_left = "10.0px"
    self.label_distr_costs.css_position = "absolute"
    self.label_distr_costs.css_top = "200.0px"
    self.label_distr_costs.css_width = "290.0px"
    self.label_distr_costs.text = "Costs (total):"
    self.label_distr_costs.variable_name = "label_distr_costs"
    container0.append(self.label_distr_costs, 'label_distr_costs')
    self.label_distr_sl = Label()
    self.label_distr_sl.attr_class = "Label"
    self.label_distr_sl.attr_editor_newclass = False
    self.label_distr_sl.css_font_family = "tahoma"
    self.label_distr_sl.css_font_size = "18px"
    self.label_distr_sl.css_height = "30.0px"
    self.label_distr_sl.css_left = "10.0px"
    self.label_distr_sl.css_position = "absolute"
    self.label_distr_sl.css_top = "240.0px"
    self.label_distr_sl.css_width = "290.0px"
    self.label_distr_sl.text = "SL:"
    self.label_distr_sl.variable_name = "label_distr_sl"
    container0.append(self.label_distr_sl, 'label_distr_sl')
    label_distr_holding_rate = Label()
    label_distr_holding_rate.attr_class = "Label"
    label_distr_holding_rate.attr_editor_newclass = False
    label_distr_holding_rate.css_font_family = "tahoma"
    label_distr_holding_rate.css_font_size = "12px"
    label_distr_holding_rate.css_height = "25.0px"
    label_distr_holding_rate.css_left = "520px"
    label_distr_holding_rate.css_position = "absolute"
    label_distr_holding_rate.css_top = "275.0px"
    label_distr_holding_rate.css_width = "270px"
    label_distr_holding_rate.set_text("Holding costs rate: "  + str(distr_remi_st.HOLDINGRATE))
    label_distr_holding_rate.variable_name = "label_distr_holding_rate"
    container0.append(label_distr_holding_rate, 'label_distr_holding_rate')
    label_distr_backlog_rate = Label()
    label_distr_backlog_rate.attr_class = "Label"
    label_distr_backlog_rate.attr_editor_newclass = False
    label_distr_backlog_rate.css_font_family = "tahoma"
    label_distr_backlog_rate.css_font_size = "12px"
    label_distr_backlog_rate.css_height = "25.0px"
    label_distr_backlog_rate.css_left = "520.0px"
    label_distr_backlog_rate.css_position = "absolute"
    label_distr_backlog_rate.css_top = "305.0px"
    label_distr_backlog_rate.css_width = "270.0px"
    label_distr_backlog_rate.set_text("Backlog costs rate: " + str(distr_remi_st.BACKLOGRATE))
    label_distr_backlog_rate.variable_name = "label_distr_backlog_rate"
    container0.append(label_distr_backlog_rate, 'label_distr_backlog_rate')
    self.button_distr_order = Button()
    self.button_distr_order.attr_class = "Button"
    self.button_distr_order.attr_editor_newclass = False
    self.button_distr_order.css_background_color = "rgb(158,176,253)"
    self.button_distr_order.css_border_style = "none"
    self.button_distr_order.css_flex = "1"
    self.button_distr_order.css_font_family = "Tahoma"
    self.button_distr_order.css_font_size = "16px"
    self.button_distr_order.css_height = "30.0px"
    self.button_distr_order.css_left = "200.0px"
    self.button_distr_order.css_position = "absolute"
    self.button_distr_order.css_top = "60.0px"
    self.button_distr_order.css_width = "100.0px"
    self.button_distr_order.text = "Order"
    self.button_distr_order.css_color = "rgb(255,255,255)"
    self.button_distr_order.variable_name = "button_distr_order"
    container0.append(self.button_distr_order, 'button_distr_order')
    self.button_distr_shipment = Button()
    self.button_distr_shipment.attr_class = "Button"
    self.button_distr_shipment.attr_editor_newclass = False
    self.button_distr_shipment.css_background_color = "rgb(158,176,253)"
    self.button_distr_shipment.css_border_style = "none"
    self.button_distr_shipment.css_flex = "1"
    self.button_distr_shipment.css_font_family = "Tahoma"
    self.button_distr_shipment.css_font_size = "16px"
    self.button_distr_shipment.css_height = "30.0px"
    self.button_distr_shipment.css_left = "200.0px"
    self.button_distr_shipment.css_position = "absolute"
    self.button_distr_shipment.css_top = "100.0px"
    self.button_distr_shipment.css_width = "100.0px"
    self.button_distr_shipment.text = "Shipment"
    self.button_distr_shipment.css_color = "rgb(255,255,255)"
    self.button_distr_shipment.variable_name = "button_distr_shipment"
    container0.append(self.button_distr_shipment, 'button_distr_shipment')
    self.button_distr_order.set_enabled(False)
    self.button_distr_update.set_enabled(False)
    self.button_distr_shipment.set_enabled(False)
    self.button_distr_order.css_background_color = "rgb(200,200,200)"
    self.button_distr_update.css_background_color = "rgb(200,200,200)"
    self.button_distr_shipment.css_background_color = "rgb(200,200,200)"
    self.button_distr_disconnect.set_enabled(False)
    self.button_distr_disconnect.css_background_color = "rgb(200,200,200)"

    self.button_distr_connect.onclick.do(functools.partial(self.on_button_distr_connect_pressed, self.textEditPassDistr,
                                                           self.textEditServerDistr, self.textEditPortDistr,
                                                           self.label_distr_info, self.button_distr_update,
                                                           self.button_distr_disconnect ))
    self.button_distr_disconnect.onclick.do(functools.partial(self.on_button_distr_disconnect_pressed,
                                                              self.button_distr_connect, self.label_distr_info))
    self.button_distr_update.onclick.do(functools.partial(self.on_button_distr_update_pressed, self.button_distr_shipment,
                                                          self.label_distr_period, self.textEditPortDistr,
                                                          self.label_distr_costs, self.label_distr_demand,
                                                          self.label_distr_inventory, self.label_distr_backlog,
                                                          self.label_distr_status))
    self.button_distr_shipment.onclick.do(functools.partial(self.on_button_distr_shipment_pressed,
                                                            self.textEditShipmentDistributor, self.label_distr_inventory,
                                                            self.label_distr_sl, self.textEditPortDistr,
                                                            self.button_distr_shipment, self.button_distr_order,
                                                            self.label_distr_backlog))
    self.button_distr_order.onclick.do(functools.partial(self.on_button_distr_order_pressed,
                                                         self.textEditOrderDistributor, self.button_distr_order,
                                                         self.textEditPortDistr))

    return container0


def on_button_distr_connect_pressed(self, widget):
    widgets = [self.textEditPassDistr, self.textEditServerDistr, self.textEditPortDistr, self.label_distr_info,
               self.button_distr_update, self.button_distr_disconnect]
    distr_remi_st.distr_remi.on_button_distr_connect_pressed(functools.partial(self, *widgets))


def on_button_distr_disconnect_pressed(self, widget):
    distr_remi_st.distr_remi.on_button_distr_disconnect_pressed(functools.partial(self, self.button_distr_connect,
                                                                                  self.label_distr_info, widget))


def on_button_distr_update_pressed(self, widget):
    widgets = [self.button_distr_shipment, self.label_distr_period, self.textEditPortDistr, self.label_distr_costs,
               self.label_distr_demand, self.label_distr_inventory, self.label_distr_backlog, self.label_distr_status]
    distr_remi_st.distr_remi.on_button_distr_update_pressed(functools.partial(self, *widgets))


def on_button_distr_place_order_pressed(self, widget):
    distr_remi_st.distr_remi.on_button_distr_order_pressed(functools.partial(self, self.textEditOrderDistributor,
                                                                             self.button_distr_order, self.textEditPortDistr))


def on_button_distr_shipment_pressed(self, widget):
    widgets = [self.textEditShipmentDistributor, self.label_distr_inventory, self.label_distr_sl, self.textEditPortDistr,
               self.button_distr_shipment, self.button_distr_order, self.label_distr_backlog]
    distr_remi_st.distr_remi.on_button_distr_shipment_pressed(functools.partial(self, *widgets))
