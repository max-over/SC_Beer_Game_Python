from remi.gui import *
import whole_remi_st
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
    label_whole_ordersize = Label()
    label_whole_ordersize.attr_class = "Label"
    label_whole_ordersize.attr_editor_newclass = False
    label_whole_ordersize.css_font_family = "Tahoma"
    label_whole_ordersize.css_font_size = "18px"
    label_whole_ordersize.css_height = "30px"
    label_whole_ordersize.css_left = "10.0px"
    label_whole_ordersize.css_position = "absolute"
    label_whole_ordersize.css_top = "55.0px"
    label_whole_ordersize.css_width = "100px"
    label_whole_ordersize.text = "Order Size:"
    label_whole_ordersize.variable_name = "label_whole_ordersize"
    container0.append(label_whole_ordersize, 'label_whole_ordersize')
    label_whole_shipment = Label()
    label_whole_shipment.attr_class = "Label"
    label_whole_shipment.attr_editor_newclass = False
    label_whole_shipment.css_font_family = "Tahoma"
    label_whole_shipment.css_font_size = "18px"
    label_whole_shipment.css_height = "30px"
    label_whole_shipment.css_left = "10.0px"
    label_whole_shipment.css_position = "absolute"
    label_whole_shipment.css_top = "95.0px"
    label_whole_shipment.css_width = "100px"
    label_whole_shipment.text = "Shipment:"
    label_whole_shipment.variable_name = "label_whole_shipment"
    container0.append(label_whole_shipment, 'label_whole_shipment')
    self.label_whole_period = Label()
    self.label_whole_period.attr_class = "Label"
    self.label_whole_period.attr_editor_newclass = False
    self.label_whole_period.css_font_family = "Tahoma"
    self.label_whole_period.css_font_size = "22px"
    self.label_whole_period.css_font_style = "normal"
    self.label_whole_period.css_font_weight = "bold"
    self.label_whole_period.css_height = "30.0px"
    self.label_whole_period.css_left = "10.0px"
    self.label_whole_period.css_position = "absolute"
    self.label_whole_period.css_top = "10.0px"
    self.label_whole_period.css_width = "280.0px"
    self.label_whole_period.text = "Current Period: 0"
    self.label_whole_period.variable_name = "label_whole_period"
    container0.append(self.label_whole_period, 'label_whole_period')
    self.textEditOrderWholesaler = TextInput()
    self.textEditOrderWholesaler.attr_class = "TextInput"
    self.textEditOrderWholesaler.attr_editor_newclass = False
    self.textEditOrderWholesaler.css_font_family = "tahoma"
    self.textEditOrderWholesaler.css_font_size = "20px"
    self.textEditOrderWholesaler.css_height = "30.0px"
    self.textEditOrderWholesaler.css_left = "110.0px"
    self.textEditOrderWholesaler.css_position = "absolute"
    self.textEditOrderWholesaler.css_text_align = "right"
    self.textEditOrderWholesaler.css_top = "60.0px"
    self.textEditOrderWholesaler.css_width = "75.0px"
    self.textEditOrderWholesaler.text = "1"
    self.textEditOrderWholesaler.variable_name = "textEditOrderWholesaler"
    container0.append(self.textEditOrderWholesaler, 'textEditOrderWholesaler')
    self.textEditShipmentWholesaler = TextInput()
    self.textEditShipmentWholesaler.attr_class = "TextInput"
    self.textEditShipmentWholesaler.attr_editor_newclass = False
    self.textEditShipmentWholesaler.css_font_family = "tahoma"
    self.textEditShipmentWholesaler.css_font_size = "20px"
    self.textEditShipmentWholesaler.css_height = "30.0px"
    self.textEditShipmentWholesaler.css_left = "110.0px"
    self.textEditShipmentWholesaler.css_position = "absolute"
    self.textEditShipmentWholesaler.css_text_align = "right"
    self.textEditShipmentWholesaler.css_top = "100.0px"
    self.textEditShipmentWholesaler.css_width = "75.0px"
    self.textEditShipmentWholesaler.text = "1"
    self.textEditShipmentWholesaler.variable_name = "textEditShipmentWholesaler"
    container0.append(self.textEditShipmentWholesaler, 'textEditShipmentWholesaler')
    self.label_whole_info = Label()
    self.label_whole_info.attr_class = "Label"
    self.label_whole_info.attr_editor_newclass = False
    self.label_whole_info.css_height = "30.0px"
    self.label_whole_info.css_left = "10.0px"
    self.label_whole_info.css_position = "absolute"
    self.label_whole_info.css_top = "555.0px"
    self.label_whole_info.text = "Info"
    self.label_whole_info.css_visibility = "hidden"
    self.label_whole_info.variable_name = "label_whole_info"
    self.label_whole_info.css_width = "300.0px"
    self.label_whole_info.css_font_family = "tahoma"
    self.label_whole_info.css_font_size = "12px"
    container0.append(self.label_whole_info, 'label_whole_info')
    label_whole_server = Label()
    label_whole_server.attr_class = "Label"
    label_whole_server.attr_editor_newclass = False
    label_whole_server.css_height = "30.0px"
    label_whole_server.css_left = "10.0px"
    label_whole_server.css_position = "absolute"
    label_whole_server.css_top = "465.0px"
    label_whole_server.css_width = "60.0px"
    label_whole_server.text = "Server:"
    label_whole_server.variable_name = "label_whole_server"
    container0.append(label_whole_server, 'label_whole_server')
    label_whole_pass = Label()
    label_whole_pass.attr_class = "Label"
    label_whole_pass.attr_editor_newclass = False
    label_whole_pass.css_height = "30.0px"
    label_whole_pass.css_left = "10.0px"
    label_whole_pass.css_position = "absolute"
    label_whole_pass.css_top = "425.0px"
    label_whole_pass.css_width = "60.0px"
    label_whole_pass.text = "Password:"
    label_whole_pass.css_font_family = "Tahoma"
    label_whole_pass.css_font_size = "14px"
    label_whole_pass.variable_name = "label_whole_pass"
    container0.append(label_whole_pass, 'label_whole_pass')
    label_whole_port = Label()
    label_whole_port.attr_class = "Label"
    label_whole_port.attr_editor_newclass = False
    label_whole_port.css_height = "30.0px"
    label_whole_port.css_left = "10.0px"
    label_whole_port.css_position = "absolute"
    label_whole_port.css_top = "510.0px"
    label_whole_port.css_width = "45.0px"
    label_whole_port.text = "Port:"
    label_whole_port.variable_name = "label_whole_port"
    container0.append(label_whole_port, 'label_whole_port')
    self.textEditServerWhole = TextInput()
    self.textEditServerWhole.attr_class = "TextInput"
    self.textEditServerWhole.attr_editor_newclass = False
    self.textEditServerWhole.css_font_family = "Tahoma"
    self.textEditServerWhole.css_height = "30.0px"
    self.textEditServerWhole.css_left = "75.0px"
    self.textEditServerWhole.css_position = "absolute"
    self.textEditServerWhole.css_text_align = "center"
    self.textEditServerWhole.css_top = "465.0px"
    self.textEditServerWhole.css_width = "225.0px"
    self.textEditServerWhole.text = "localhost"
    self.textEditServerWhole.variable_name = "textEditServerWhole"
    container0.append(self.textEditServerWhole, 'textEditServerWhole')
    self.textEditPassWhole = TextInput()
    self.textEditPassWhole.attr_class = "TextInput"
    self.textEditPassWhole.attr_editor_newclass = False
    self.textEditPassWhole.css_font_family = "Tahoma"
    self.textEditPassWhole.css_height = "30.0px"
    self.textEditPassWhole.css_left = "75.0px"
    self.textEditPassWhole.css_position = "absolute"
    self.textEditPassWhole.css_top = "425.0px"
    self.textEditPassWhole.css_width = "225.0px"
    self.textEditPassWhole.text = "passphrase"
    self.textEditPassWhole.css_text_align = "center"
    self.textEditPassWhole.variable_name = "textEditWholeDistr"
    container0.append(self.textEditPassWhole, 'textEditWholeDistr')
    self.textEditPortWhole = TextInput()
    self.textEditPortWhole.attr_class = "TextInput"
    self.textEditPortWhole.attr_editor_newclass = False
    self.textEditPortWhole.css_align_self = "center"
    self.textEditPortWhole.css_font_family = "Tahoma"
    self.textEditPortWhole.css_height = "40.0px"
    self.textEditPortWhole.css_left = "75.0px"
    self.textEditPortWhole.css_position = "absolute"
    self.textEditPortWhole.css_text_align = "center"
    self.textEditPortWhole.css_top = "510.0px"
    self.textEditPortWhole.css_width = "120.0px"
    self.textEditPortWhole.text = "5555"
    self.textEditPortWhole.variable_name = "textEditPortWhole"
    container0.append(self.textEditPortWhole, 'textEditPortWhole')
    self.button_whole_connect = Button()
    self.button_whole_connect.attr_class = "Button"
    self.button_whole_connect.css_border_style = "none"
    self.button_whole_connect.attr_editor_newclass = False
    self.button_whole_connect.css_background_color = "rgb(254,150,160)"
    self.button_whole_connect.css_font_family = "Tahoma"
    self.button_whole_connect.css_font_size = "16px"
    self.button_whole_connect.css_height = "40.0px"
    self.button_whole_connect.css_left = "210.0px"
    self.button_whole_connect.css_position = "absolute"
    self.button_whole_connect.css_top = "510.0px"
    self.button_whole_connect.css_width = "90.0px"
    self.button_whole_connect.text = "Connect"
    self.button_whole_connect.css_color = "rgb(255,255,255)"
    self.button_whole_connect.variable_name = "button_whole_connect"
    container0.append(self.button_whole_connect, 'button_whole_connect')
    self.button_whole_disconnect = Button()
    self.button_whole_disconnect.attr_class = "Button"
    self.button_whole_disconnect.css_border_style = "none"
    self.button_whole_disconnect.attr_editor_newclass = False
    self.button_whole_disconnect.css_background_color = "rgb(254,150,160)"
    self.button_whole_disconnect.css_font_family = "Tahoma"
    self.button_whole_disconnect.css_font_size = "16px"
    self.button_whole_disconnect.css_height = "40.0px"
    self.button_whole_disconnect.css_left = "690.0px"
    self.button_whole_disconnect.css_position = "absolute"
    self.button_whole_disconnect.css_top = "510.0px"
    self.button_whole_disconnect.css_width = "100.0px"
    self.button_whole_disconnect.text = "Disconnect"
    self.button_whole_disconnect.css_color = "rgb(255,255,255)"
    self.button_whole_disconnect.variable_name = "button_whole_disconnect"
    container0.append(self.button_whole_disconnect, 'button_whole_disconnect')
    self.button_whole_update = Button()
    self.button_whole_update.attr_class = "Button"
    self.button_whole_update.css_border_style = "none"
    self.button_whole_update.attr_editor_newclass = False
    self.button_whole_update.css_background_color = "rgb(254,150,160)"
    self.button_whole_update.css_font_family = "Tahoma"
    self.button_whole_update.css_font_size = "16px"
    self.button_whole_update.css_height = "40.0px"
    self.button_whole_update.css_left = "10.0px"
    self.button_whole_update.css_position = "absolute"
    self.button_whole_update.css_top = "140.0px"
    self.button_whole_update.css_width = "100.0px"
    self.button_whole_update.text = "Update"
    self.button_whole_update.css_color = "rgb(255,255,255)"
    self.button_whole_update.variable_name = "button_whole_update"
    container0.append(self.button_whole_update, 'button_whole_update')
    label_whole_turnstatus = Label()
    label_whole_turnstatus.attr_class = "Label"
    label_whole_turnstatus.attr_editor_newclass = False
    label_whole_turnstatus.css_font_family = "Tahoma"
    label_whole_turnstatus.css_font_size = "22px"
    label_whole_turnstatus.css_font_weight = "bold"
    label_whole_turnstatus.css_height = "40.0px"
    label_whole_turnstatus.css_left = "520.0px"
    label_whole_turnstatus.css_position = "absolute"
    label_whole_turnstatus.css_top = "10.0px"
    label_whole_turnstatus.css_width = "160.0px"
    label_whole_turnstatus.text = "Turn Status"
    label_whole_turnstatus.variable_name = "label_whole_turnstatus"
    container0.append(label_whole_turnstatus, 'label_whole_turnstatus')
    label_whole_leadtime = Label()
    label_whole_leadtime.attr_class = "Label"
    label_whole_leadtime.attr_editor_newclass = False
    label_whole_leadtime.css_font_family = "tahoma"
    label_whole_leadtime.css_font_size = "14px"
    label_whole_leadtime.css_font_weight = "bold"
    label_whole_leadtime.css_height = "30.0px"
    label_whole_leadtime.css_left = "320.0px"
    label_whole_leadtime.css_position = "absolute"
    label_whole_leadtime.css_top = "50.0px"
    label_whole_leadtime.css_width = "190.0px"
    label_whole_leadtime.set_text("Leadtime to Plant: " + str(whole_remi_st.LEADTIMEUP))
    label_whole_leadtime.variable_name = "label_whole_leadtime"
    container0.append(label_whole_leadtime, 'label_whole_leadtime')
    self.label_whole_status = Label()
    self.label_whole_status.attr_class = "Label"
    self.label_whole_status.attr_editor_newclass = False
    self.label_whole_status.css_font_family = "tahoma"
    self.label_whole_status.css_font_size = "14px"
    self.label_whole_status.css_height = "260.0px"
    self.label_whole_status.css_left = "520.0px"
    self.label_whole_status.css_position = "absolute"
    self.label_whole_status.css_top = "50.0px"
    self.label_whole_status.css_white_space = "pre-wrap"
    self.label_whole_status.css_width = "270.0px"
    self.label_whole_status.text = "Turn status info"
    self.label_whole_status.variable_name = "label_whole_status"
    container0.append(self.label_whole_status, 'label_whole_status')
    label_whole_intransit = Label()
    label_whole_intransit.attr_class = "Label"
    label_whole_intransit.attr_editor_newclass = False
    label_whole_intransit.css_font_family = "tahoma"
    label_whole_intransit.css_font_size = "14px"
    label_whole_intransit.css_font_weight = "bold"
    label_whole_intransit.css_height = "30.0px"
    label_whole_intransit.css_left = "320.0px"
    label_whole_intransit.css_position = "absolute"
    label_whole_intransit.css_top = "10.0px"
    label_whole_intransit.css_width = "130.0px"
    label_whole_intransit.text = "In transit:"
    label_whole_intransit.variable_name = "label_whole_intransit"
    label_whole_intransit.css_visibility = "hidden"
    container0.append(label_whole_intransit, 'label_whole_intransit')
    self.label_whole_backlog = Label()
    self.label_whole_backlog.attr_class = "Label"
    self.label_whole_backlog.attr_editor_newclass = False
    self.label_whole_backlog.css_font_family = "tahoma"
    self.label_whole_backlog.css_font_size = "14px"
    self.label_whole_backlog.css_font_weight = "bold"
    self.label_whole_backlog.css_height = "30.0px"
    self.label_whole_backlog.css_left = "320.0px"
    self.label_whole_backlog.css_position = "absolute"
    self.label_whole_backlog.css_top = "90.0px"
    self.label_whole_backlog.css_width = "190.0px"
    self.label_whole_backlog.text = "Backlog (total):"
    self.label_whole_backlog.variable_name = "label_whole_backlog"
    container0.append(self.label_whole_backlog, 'label_whole_backlog')
    self.label_whole_inventory = Label()
    self.label_whole_inventory.attr_class = "Label"
    self.label_whole_inventory.attr_editor_newclass = False
    self.label_whole_inventory.css_font_family = "tahoma"
    self.label_whole_inventory.css_font_size = "14px"
    self.label_whole_inventory.css_font_weight = "bold"
    self.label_whole_inventory.css_height = "30.0px"
    self.label_whole_inventory.css_left = "320.0px"
    self.label_whole_inventory.css_position = "absolute"
    self.label_whole_inventory.css_top = "130.0px"
    self.label_whole_inventory.css_width = "190.0px"
    self.label_whole_inventory.text = "Inventory:"
    self.label_whole_inventory.variable_name = "label_whole_inventory"
    container0.append(self.label_whole_inventory, 'label_whole_inventory')
    self.label_whole_demand = Label()
    self.label_whole_demand.attr_class = "Label"
    self.label_whole_demand.attr_editor_newclass = False
    self.label_whole_demand.css_font_family = "tahoma"
    self.label_whole_demand.css_font_size = "14px"
    self.label_whole_demand.css_font_weight = "bold"
    self.label_whole_demand.css_height = "30.0px"
    self.label_whole_demand.css_left = "320.0px"
    self.label_whole_demand.css_position = "absolute"
    self.label_whole_demand.css_top = "170.0px"
    self.label_whole_demand.css_width = "190.0px"
    self.label_whole_demand.text = "Demand:"
    self.label_whole_demand.variable_name = "label_whole_demand"
    container0.append(self.label_whole_demand, 'label_whole_demand')
    self.label_whole_costs = Label()
    self.label_whole_costs.attr_class = "Label"
    self.label_whole_costs.attr_editor_newclass = False
    self.label_whole_costs.css_font_family = "tahoma"
    self.label_whole_costs.css_font_size = "18px"
    self.label_whole_costs.css_height = "30.0px"
    self.label_whole_costs.css_left = "10.0px"
    self.label_whole_costs.css_position = "absolute"
    self.label_whole_costs.css_top = "200.0px"
    self.label_whole_costs.css_width = "290.0px"
    self.label_whole_costs.text = "Costs (total):"
    self.label_whole_costs.variable_name = "label_whole_costs"
    container0.append(self.label_whole_costs, 'label_whole_costs')
    self.label_whole_sl = Label()
    self.label_whole_sl.attr_class = "Label"
    self.label_whole_sl.attr_editor_newclass = False
    self.label_whole_sl.css_font_family = "tahoma"
    self.label_whole_sl.css_font_size = "18px"
    self.label_whole_sl.css_height = "30.0px"
    self.label_whole_sl.css_left = "10.0px"
    self.label_whole_sl.css_position = "absolute"
    self.label_whole_sl.css_top = "240.0px"
    self.label_whole_sl.css_width = "290.0px"
    self.label_whole_sl.text = "SL:"
    self.label_whole_sl.variable_name = "label_whole_sl"
    container0.append(self.label_whole_sl, 'label_whole_sl')
    label_whole_holding_rate = Label()
    label_whole_holding_rate.attr_class = "Label"
    label_whole_holding_rate.attr_editor_newclass = False
    label_whole_holding_rate.css_font_family = "tahoma"
    label_whole_holding_rate.css_font_size = "12px"
    label_whole_holding_rate.css_height = "25.0px"
    label_whole_holding_rate.css_left = "520px"
    label_whole_holding_rate.css_position = "absolute"
    label_whole_holding_rate.css_top = "275.0px"
    label_whole_holding_rate.css_width = "270px"
    label_whole_holding_rate.set_text("Holding costs rate: " + str(whole_remi_st.HOLDINGRATE))
    label_whole_holding_rate.variable_name = "label_whole_holding_rate"
    container0.append(label_whole_holding_rate, 'label_whole_holding_rate')
    label_whole_backlog_rate = Label()
    label_whole_backlog_rate.attr_class = "Label"
    label_whole_backlog_rate.attr_editor_newclass = False
    label_whole_backlog_rate.css_font_family = "tahoma"
    label_whole_backlog_rate.css_font_size = "12px"
    label_whole_backlog_rate.css_height = "25.0px"
    label_whole_backlog_rate.css_left = "520.0px"
    label_whole_backlog_rate.css_position = "absolute"
    label_whole_backlog_rate.css_top = "305.0px"
    label_whole_backlog_rate.css_width = "270.0px"
    label_whole_backlog_rate.set_text("Backlog costs rate: " + str(whole_remi_st.BACKLOGRATE))
    label_whole_backlog_rate.variable_name = "label_whole_backlog_rate"
    container0.append(label_whole_backlog_rate, 'label_whole_backlog_rate')
    self.button_whole_order = Button()
    self.button_whole_order.attr_class = "Button"
    self.button_whole_order.attr_editor_newclass = False
    self.button_whole_order.css_background_color = "rgb(254,150,160)"
    self.button_whole_order.css_border_style = "none"
    self.button_whole_order.css_flex = "1"
    self.button_whole_order.css_font_family = "Tahoma"
    self.button_whole_order.css_font_size = "16px"
    self.button_whole_order.css_height = "30.0px"
    self.button_whole_order.css_left = "200.0px"
    self.button_whole_order.css_position = "absolute"
    self.button_whole_order.css_top = "60.0px"
    self.button_whole_order.css_width = "100.0px"
    self.button_whole_order.text = "Order"
    self.button_whole_order.css_color = "rgb(255,255,255)"
    self.button_whole_order.variable_name = "button_whole_order"
    container0.append(self.button_whole_order, 'button_whole_order')
    self.button_whole_shipment = Button()
    self.button_whole_shipment.attr_class = "Button"
    self.button_whole_shipment.attr_editor_newclass = False
    self.button_whole_shipment.css_background_color = "rgb(254,150,160)"
    self.button_whole_shipment.css_border_style = "none"
    self.button_whole_shipment.css_flex = "1"
    self.button_whole_shipment.css_font_family = "Tahoma"
    self.button_whole_shipment.css_font_size = "16px"
    self.button_whole_shipment.css_height = "30.0px"
    self.button_whole_shipment.css_left = "200.0px"
    self.button_whole_shipment.css_position = "absolute"
    self.button_whole_shipment.css_top = "100.0px"
    self.button_whole_shipment.css_width = "100.0px"
    self.button_whole_shipment.text = "Shipment"
    self.button_whole_shipment.css_color = "rgb(255,255,255)"
    self.button_whole_shipment.variable_name = "button_whole_shipment"
    container0.append(self.button_whole_shipment, 'button_whole_shipment')

    self.button_whole_order.set_enabled(False)
    self.button_whole_update.set_enabled(False)
    self.button_whole_shipment.set_enabled(False)
    self.button_whole_order.css_background_color = "rgb(200,200,200)"
    self.button_whole_update.css_background_color = "rgb(200,200,200)"
    self.button_whole_shipment.css_background_color = "rgb(200,200,200)"
    self.button_whole_disconnect.set_enabled(False)
    self.button_whole_disconnect.css_background_color = "rgb(200,200,200)"

    self.button_whole_connect.onclick.do(functools.partial(self.on_button_whole_connect_pressed, self.textEditPassWhole,
                                                           self.textEditServerWhole, self.textEditPortWhole,
                                                           self.label_whole_info, self.button_whole_update,
                                                           self.button_whole_disconnect))
    self.button_whole_disconnect.onclick.do(functools.partial(self.on_button_whole_disconnect_pressed,
                                                              self.button_whole_connect, self.label_whole_info))
    self.button_whole_update.onclick.do(functools.partial(self.on_button_whole_update_pressed, self.button_whole_shipment,
                                                          self.label_whole_period, self.textEditPortWhole,
                                                          self.label_whole_costs, self.label_whole_demand,
                                                          self.label_whole_inventory, self.label_whole_backlog,
                                                          self.label_whole_status))
    self.button_whole_shipment.onclick.do(functools.partial(self.on_button_whole_shipment_pressed,
                                                            self.textEditShipmentWholesaler, self.label_whole_inventory,
                                                            self.label_whole_sl, self.textEditPortWhole,
                                                            self.button_whole_shipment, self.button_whole_order,
                                                            self.label_whole_backlog))
    self.button_whole_order.onclick.do(functools.partial(self.on_button_whole_order_pressed,
                                                         self.textEditOrderWholesaler, self.button_whole_order,
                                                         self.textEditPortWhole))

    self.container0 = container0
    return self.container0


def on_button_whole_connect_pressed(self, widget):
    widgets = [self.textEditPassWhole, self.textEditServerWhole, self.textEditPortWhole, self.label_whole_info,
               self.button_whole_update, self.button_whole_disconnect]
    whole_remi_st.whole_remi.on_button_whole_connect_pressed(functools.partial(self, *widgets))


def on_button_whole_disconnect_pressed(self, widget):
    whole_remi_st.whole_remi.on_button_whole_disconnect_pressed(functools.partial(self, self.button_whole_connect,
                                                                                  self.label_whole_info))


def on_button_whole_update_pressed(self, widget):
    widgets = [self.button_whole_shipment, self.label_whole_period, self.textEditPortWhole, self.label_whole_costs,
               self.label_whole_demand, self.label_whole_inventory, self.label_whole_backlog, self.label_whole_status]
    whole_remi_st.whole_remi.on_button_whole_update_pressed(functools.partial(self, *widgets))


def on_button_whole_place_order_pressed(self, widget):
    whole_remi_st.whole_remi.on_button_whole_order_pressed(functools.partial(self, self.textEditOrderWholesaler,
                                                                             self.button_whole_order, self.textEditPortWhole))


def on_button_whole_shipment_pressed(self, widget):
    widgets = [self.textEditShipmentWholesaler, self.label_whole_inventory, self.label_whole_sl, self.textEditPortWhole,
               self.button_whole_shipment, self.button_whole_order, self.label_whole_backlog]
    whole_remi_st.whole_remi.on_button_whole_shipment_pressed(functools.partial(self, *widgets))
