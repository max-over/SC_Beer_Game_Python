from remi.gui import *
import ret_remi_st
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
    label_ret_ordersize = Label()
    label_ret_ordersize.attr_class = "Label"
    label_ret_ordersize.attr_editor_newclass = False
    label_ret_ordersize.css_font_family = "Tahoma"
    label_ret_ordersize.css_font_size = "18px"
    label_ret_ordersize.css_height = "30px"
    label_ret_ordersize.css_left = "10.0px"
    label_ret_ordersize.css_position = "absolute"
    label_ret_ordersize.css_top = "60.0px"
    label_ret_ordersize.css_width = "100px"
    label_ret_ordersize.text = "Order Size:"
    label_ret_ordersize.variable_name = "label_ret_ordersize"
    container0.append(label_ret_ordersize, 'label_ret_ordersize')
    label_ret_period = Label()
    label_ret_period.attr_class = "Label"
    label_ret_period.attr_editor_newclass = False
    label_ret_period.css_font_family = "tahoma"
    label_ret_period.css_font_size = "16px"
    label_ret_period.css_font_weight = "bold"
    label_ret_period.css_height = "35.0px"
    label_ret_period.css_left = "320.0px"
    label_ret_period.css_position = "absolute"
    label_ret_period.css_top = "270.0px"
    label_ret_period.css_width = "185.0px"
    label_ret_period.text = "Stock Structure:"
    label_ret_period.variable_name = "label_ret_period"
    container0.append(label_ret_period, 'label_ret_period')
    self.textEditOrderRetailer = TextInput()
    self.textEditOrderRetailer.attr_class = "TextInput"
    self.textEditOrderRetailer.attr_editor_newclass = False
    self.textEditOrderRetailer.css_font_family = "tahoma"
    self.textEditOrderRetailer.css_font_size = "20px"
    self.textEditOrderRetailer.css_height = "30.0px"
    self.textEditOrderRetailer.css_left = "110.0px"
    self.textEditOrderRetailer.css_position = "absolute"
    self.textEditOrderRetailer.css_text_align = "right"
    self.textEditOrderRetailer.css_top = "60.0px"
    self.textEditOrderRetailer.css_width = "75.0px"
    self.textEditOrderRetailer.text = "1"
    self.textEditOrderRetailer.variable_name = "textEditOrderRetailer"
    container0.append(self.textEditOrderRetailer, 'textEditOrderRetailer')
    self.label_ret_info = Label()
    self.label_ret_info.attr_class = "Label"
    self.label_ret_info.attr_editor_newclass = False
    self.label_ret_info.css_height = "30.0px"
    self.label_ret_info.css_left = "10.0px"
    self.label_ret_info.css_position = "absolute"
    self.label_ret_info.css_top = "555.0px"
    self.label_ret_info.text = "Info"
    self.label_ret_info.css_visibility = "hidden"
    self.label_ret_info.variable_name = "label_ret_info"
    self.label_ret_info.css_width = "300.0px"
    self.label_ret_info.css_font_family = "tahoma"
    self.label_ret_info.css_font_size = "12px"
    container0.append(self.label_ret_info, 'label_ret_info')
    label_ret_server = Label()
    label_ret_server.attr_class = "Label"
    label_ret_server.attr_editor_newclass = False
    label_ret_server.css_height = "30.0px"
    label_ret_server.css_left = "10.0px"
    label_ret_server.css_position = "absolute"
    label_ret_server.css_top = "465.0px"
    label_ret_server.css_width = "60.0px"
    label_ret_server.text = "Server:"
    label_ret_server.css_font_family = "tahoma"
    label_ret_server.css_font_size = "14px"
    label_ret_server.variable_name = "label_ret_server"
    container0.append(label_ret_server, 'label_ret_server')
    label_ret_pass = Label()
    label_ret_pass.attr_class = "Label"
    label_ret_pass.attr_editor_newclass = False
    label_ret_pass.css_height = "30.0px"
    label_ret_pass.css_left = "10.0px"
    label_ret_pass.css_position = "absolute"
    label_ret_pass.css_top = "425.0px"
    label_ret_pass.css_width = "60.0px"
    label_ret_pass.text = "Password:"
    label_ret_pass.css_font_family = "Tahoma"
    label_ret_pass.css_font_size = "14px"
    label_ret_pass.variable_name = "label_ret_pass"
    container0.append(label_ret_pass, 'label_ret_pass')
    label_ret_port = Label()
    label_ret_port.attr_class = "Label"
    label_ret_port.attr_editor_newclass = False
    label_ret_port.css_height = "30.0px"
    label_ret_port.css_left = "10.0px"
    label_ret_port.css_position = "absolute"
    label_ret_port.css_top = "510.0px"
    label_ret_port.css_width = "45.0px"
    label_ret_port.text = "Port:"
    label_ret_port.variable_name = "label_ret_port"
    label_ret_port.css_font_family = "tahoma"
    label_ret_port.css_font_size = "14px"
    container0.append(label_ret_port, 'label_ret_port')
    self.textEditServerRet = TextInput()
    self.textEditServerRet.attr_class = "TextInput"
    self.textEditServerRet.attr_editor_newclass = False
    self.textEditServerRet.css_font_family = "tahoma"
    self.textEditServerRet.css_height = "30.0px"
    self.textEditServerRet.css_left = "75.0px"
    self.textEditServerRet.css_position = "absolute"
    self.textEditServerRet.css_text_align = "center"
    self.textEditServerRet.css_top = "465.0px"
    self.textEditServerRet.css_width = "225.0px"
    self.textEditServerRet.text = "localhost"
    self.textEditServerRet.variable_name = "textEditServerRet"
    container0.append(self.textEditServerRet, 'textEditServerRet')
    self.textEditPassRet = TextInput()
    self.textEditPassRet.attr_class = "TextInput"
    self.textEditPassRet.attr_editor_newclass = False
    self.textEditPassRet.css_font_family = "Tahoma"
    self.textEditPassRet.css_height = "30.0px"
    self.textEditPassRet.css_left = "75.0px"
    self.textEditPassRet.css_position = "absolute"
    self.textEditPassRet.css_top = "425.0px"
    self.textEditPassRet.css_width = "225.0px"
    self.textEditPassRet.text = "passphrase"
    self.textEditPassRet.css_text_align = "center"
    self.textEditPassRet.variable_name = "textEditPassRet"
    container0.append(self.textEditPassRet, 'textEditPassRet')
    self.textEditPortRet = TextInput()
    self.textEditPortRet.attr_class = "TextInput"
    self.textEditPortRet.attr_editor_newclass = False
    self.textEditPortRet.css_align_self = "center"
    self.textEditPortRet.css_font_family = "tahoma"
    self.textEditPortRet.css_height = "40.0px"
    self.textEditPortRet.css_left = "75.0px"
    self.textEditPortRet.css_position = "absolute"
    self.textEditPortRet.css_text_align = "center"
    self.textEditPortRet.css_top = "510.0px"
    self.textEditPortRet.css_width = "120.0px"
    self.textEditPortRet.text = "5555"
    self.textEditPortRet.variable_name = "textEditPortRet"
    container0.append(self.textEditPortRet, 'textEditPortRet')
    self.button_ret_connect = Button()
    self.button_ret_connect.attr_class = "Button"
    self.button_ret_connect.css_border_style = "none"
    self.button_ret_connect.attr_editor_newclass = False
    self.button_ret_connect.css_background_color = "rgb(0,200,200)"
    self.button_ret_connect.css_font_family = "Tahoma"
    self.button_ret_connect.css_font_size = "16px"
    self.button_ret_connect.css_height = "40.0px"
    self.button_ret_connect.css_left = "210.0px"
    self.button_ret_connect.css_position = "absolute"
    self.button_ret_connect.css_top = "510.0px"
    self.button_ret_connect.css_width = "95.0px"
    self.button_ret_connect.text = "Connect"
    self.button_ret_connect.variable_name = "button_ret_connect"
    self.button_ret_connect.css_color = "rgb(255,255,255)"
    container0.append(self.button_ret_connect, 'button_ret_connect')
    self.button_ret_disconnect = Button()
    self.button_ret_disconnect.attr_class = "Button"
    self.button_ret_disconnect.css_border_style = "none"
    self.button_ret_disconnect.attr_editor_newclass = False
    self.button_ret_disconnect.css_font_family = "Tahoma"
    self.button_ret_disconnect.css_font_size = "16px"
    self.button_ret_disconnect.css_height = "40.0px"
    self.button_ret_disconnect.css_left = "690.0px"
    self.button_ret_disconnect.css_position = "absolute"
    self.button_ret_disconnect.css_top = "10.0px"
    self.button_ret_disconnect.css_width = "100.0px"
    self.button_ret_disconnect.text = "Disconnect"
    self.button_ret_disconnect.variable_name = "button_ret_disconnect"
    self.button_ret_disconnect.css_background_color = "rgb(0,200,200)"
    self.button_ret_disconnect.css_color = "rgb(255,255,255)"
    container0.append(self.button_ret_disconnect, 'button_ret_disconnect')
    self.button_ret_update = Button()
    self.button_ret_update.attr_class = "Button"
    self.button_ret_update.css_border_style = "none"
    self.button_ret_update.attr_editor_newclass = False
    self.button_ret_update.css_background_color = "rgb(0,200,200)"
    self.button_ret_update.css_font_family = "Tahoma"
    self.button_ret_update.css_font_size = "16px"
    self.button_ret_update.css_height = "40.0px"
    self.button_ret_update.css_left = "690.0px"
    self.button_ret_update.css_position = "absolute"
    self.button_ret_update.css_top = "510.0px"
    self.button_ret_update.css_width = "100.0px"
    self.button_ret_update.text = "Update"
    self.button_ret_update.variable_name = "button_ret_update"
    self.button_ret_update.css_color = "rgb(255,255,255)"
    container0.append(self.button_ret_update, 'button_ret_update')
    label_ret_turnstatus = Label()
    label_ret_turnstatus.attr_class = "Label"
    label_ret_turnstatus.attr_editor_newclass = False
    label_ret_turnstatus.css_font_family = "Tahoma"
    label_ret_turnstatus.css_font_size = "22px"
    label_ret_turnstatus.css_font_weight = "bold"
    label_ret_turnstatus.css_height = "40.0px"
    label_ret_turnstatus.css_left = "520.0px"
    label_ret_turnstatus.css_position = "absolute"
    label_ret_turnstatus.css_top = "10.0px"
    label_ret_turnstatus.css_width = "160.0px"
    label_ret_turnstatus.text = "Turn Status"
    label_ret_turnstatus.variable_name = "label_ret_turnstatus"
    container0.append(label_ret_turnstatus, 'label_ret_turnstatus')
    label_ret_leadtime = Label()
    label_ret_leadtime.attr_class = "Label"
    label_ret_leadtime.attr_editor_newclass = False
    label_ret_leadtime.css_font_family = "tahoma"
    label_ret_leadtime.css_font_size = "14px"
    label_ret_leadtime.css_font_weight = "bold"
    label_ret_leadtime.css_height = "30.0px"
    label_ret_leadtime.css_left = "320.0px"
    label_ret_leadtime.css_position = "absolute"
    label_ret_leadtime.css_top = "50.0px"
    label_ret_leadtime.css_width = "190.0px"
    label_ret_leadtime.set_text("Leadtime to Distributor: " + str(ret_remi_st.LEADTIMEUP))
    label_ret_leadtime.variable_name = "label_ret_leadtime"
    container0.append(label_ret_leadtime, 'label_ret_leadtime')
    self.label_ret_status = Label()
    self.label_ret_status.attr_class = "Label"
    self.label_ret_status.attr_editor_newclass = False
    self.label_ret_status.css_font_family = "tahoma"
    self.label_ret_status.css_font_size = "14px"
    self.label_ret_status.css_height = "260.0px"
    self.label_ret_status.css_left = "520.0px"
    self.label_ret_status.css_position = "absolute"
    self.label_ret_status.css_top = "50.0px"
    self.label_ret_status.css_width = "270.0px"
    self.label_ret_status.text = "Turn status info"
    self.label_ret_status.css_white_space = "pre-wrap"
    self.label_ret_status.variable_name = "label_ret_status"
    container0.append(self.label_ret_status, 'label_ret_status')
    label_ret_intransit = Label()
    label_ret_intransit.attr_class = "Label"
    label_ret_intransit.attr_editor_newclass = False
    label_ret_intransit.css_font_family = "tahoma"
    label_ret_intransit.css_font_size = "14px"
    label_ret_intransit.css_font_weight = "bold"
    label_ret_intransit.css_height = "30.0px"
    label_ret_intransit.css_left = "320.0px"
    label_ret_intransit.css_position = "absolute"
    label_ret_intransit.css_top = "10.0px"
    label_ret_intransit.css_width = "130.0px"
    label_ret_intransit.text = "In transit:"
    label_ret_intransit.variable_name = "label_ret_intransit"
    label_ret_intransit.css_visibility = "hidden"
    container0.append(label_ret_intransit, 'label_ret_intransit')
    self.label_ret_backlog = Label()
    self.label_ret_backlog.attr_class = "Label"
    self.label_ret_backlog.attr_editor_newclass = False
    self.label_ret_backlog.css_font_family = "tahoma"
    self.label_ret_backlog.css_font_size = "14px"
    self.label_ret_backlog.css_font_weight = "bold"
    self.label_ret_backlog.css_height = "30.0px"
    self.label_ret_backlog.css_left = "320.0px"
    self.label_ret_backlog.css_position = "absolute"
    self.label_ret_backlog.css_top = "90.0px"
    self.label_ret_backlog.css_width = "190.0px"
    self.label_ret_backlog.text = "Lost sales (total):"
    self.label_ret_backlog.variable_name = "label_ret_backlog"
    container0.append(self.label_ret_backlog, 'label_ret_backlog')
    self.label_ret_inventory = Label()
    self.label_ret_inventory.attr_class = "Label"
    self.label_ret_inventory.attr_editor_newclass = False
    self.label_ret_inventory.css_font_family = "tahoma"
    self.label_ret_inventory.css_font_size = "14px"
    self.label_ret_inventory.css_font_weight = "bold"
    self.label_ret_inventory.css_height = "30.0px"
    self.label_ret_inventory.css_left = "320.0px"
    self.label_ret_inventory.css_position = "absolute"
    self.label_ret_inventory.css_top = "130.0px"
    self.label_ret_inventory.css_width = "190.0px"
    self.label_ret_inventory.text = "Inventory:"
    self.label_ret_inventory.variable_name = "label_ret_inventory"
    container0.append(self.label_ret_inventory, 'label_ret_inventory')
    self.label_ret_demand = Label()
    self.label_ret_demand.attr_class = "Label"
    self.label_ret_demand.attr_editor_newclass = False
    self.label_ret_demand.css_font_family = "tahoma"
    self.label_ret_demand.css_font_size = "14px"
    self.label_ret_demand.css_font_weight = "bold"
    self.label_ret_demand.css_height = "30.0px"
    self.label_ret_demand.css_left = "320.0px"
    self.label_ret_demand.css_position = "absolute"
    self.label_ret_demand.css_top = "170.0px"
    self.label_ret_demand.css_width = "190.0px"
    self.label_ret_demand.text = "Demand:"
    self.label_ret_demand.variable_name = "label_ret_demand"
    container0.append(self.label_ret_demand, 'label_ret_demand')
    self.label_ret_costs = Label()
    self.label_ret_costs.attr_class = "Label"
    self.label_ret_costs.attr_editor_newclass = False
    self.label_ret_costs.css_font_family = "tahoma"
    self.label_ret_costs.css_font_size = "18px"
    self.label_ret_costs.css_height = "30.0px"
    self.label_ret_costs.css_left = "10.0px"
    self.label_ret_costs.css_position = "absolute"
    self.label_ret_costs.css_top = "100.0px"
    self.label_ret_costs.css_width = "290.0px"
    self.label_ret_costs.text = "Costs (total):"
    self.label_ret_costs.variable_name = "label_ret_costs"
    container0.append(self.label_ret_costs, 'label_ret_costs')
    self.label_ret_sl = Label()
    self.label_ret_sl.attr_class = "Label"
    self.label_ret_sl.attr_editor_newclass = False
    self.label_ret_sl.css_font_family = "tahoma"
    self.label_ret_sl.css_font_size = "18px"
    self.label_ret_sl.css_height = "30.0px"
    self.label_ret_sl.css_left = "10.0px"
    self.label_ret_sl.css_position = "absolute"
    self.label_ret_sl.css_top = "140.0px"
    self.label_ret_sl.css_width = "290.0px"
    self.label_ret_sl.text = "SL:"
    self.label_ret_sl.variable_name = "label_ret_sl"
    container0.append(self.label_ret_sl, 'label_ret_sl')
    label_ret_structure = Label()
    label_ret_structure.attr_class = "Label"
    label_ret_structure.attr_editor_newclass = False
    label_ret_structure.css_font_family = "tahoma"
    label_ret_structure.css_font_size = "14px"
    label_ret_structure.css_font_weight = "bold"
    label_ret_structure.css_height = "30.0px"
    label_ret_structure.css_left = "320.0px"
    label_ret_structure.css_position = "absolute"
    label_ret_structure.css_top = "280.0px"
    label_ret_structure.css_width = "185.0px"
    label_ret_structure.text = "Stock structure:"
    label_ret_structure.variable_name = "label_ret_structure"
    container0.append(label_ret_structure, 'label_ret_structure')
    self.label_ret_stock_structure = Label()
    self.label_ret_stock_structure.attr_class = "Label"
    self.label_ret_stock_structure.attr_editor_newclass = False
    self.label_ret_stock_structure.css_font_family = "tahoma"
    self.label_ret_stock_structure.css_font_size = "12px"
    self.label_ret_stock_structure.css_height = "285.0px"
    self.label_ret_stock_structure.css_left = "320.0px"
    self.label_ret_stock_structure.css_position = "absolute"
    self.label_ret_stock_structure.css_top = "305.0px"
    self.label_ret_stock_structure.css_width = "205.0px"
    self.label_ret_stock_structure.text = "stock:"
    self.label_ret_stock_structure.css_white_space = "pre-wrap"
    self.label_ret_stock_structure.variable_name = "label_ret_stock_structure"
    container0.append(self.label_ret_stock_structure, 'label_ret_stock_structure')
    label_ret_holding_rate = Label()
    label_ret_holding_rate.attr_class = "Label"
    label_ret_holding_rate.attr_editor_newclass = False
    label_ret_holding_rate.css_font_family = "tahoma"
    label_ret_holding_rate.css_font_size = "12px"
    label_ret_holding_rate.css_height = "25.0px"
    label_ret_holding_rate.css_left = "520px"
    label_ret_holding_rate.css_position = "absolute"
    label_ret_holding_rate.css_top = "275.0px"
    label_ret_holding_rate.css_width = "270px"
    label_ret_holding_rate.set_text("Holding costs rate: " + str(ret_remi_st.HOLDINGRATE))
    label_ret_holding_rate.variable_name = "label_ret_holding_rate"
    container0.append(label_ret_holding_rate, 'label_ret_holding_rate')
    label_ret_backlog_rate = Label()
    label_ret_backlog_rate.attr_class = "Label"
    label_ret_backlog_rate.attr_editor_newclass = False
    label_ret_backlog_rate.css_font_family = "tahoma"
    label_ret_backlog_rate.css_font_size = "12px"
    label_ret_backlog_rate.css_height = "25.0px"
    label_ret_backlog_rate.css_left = "520.0px"
    label_ret_backlog_rate.css_position = "absolute"
    label_ret_backlog_rate.css_top = "305.0px"
    label_ret_backlog_rate.css_width = "270.0px"
    label_ret_backlog_rate.set_text("Lost sales costs rate: " + str(ret_remi_st.BACKLOGRATE))
    label_ret_backlog_rate.variable_name = "label_ret_backlog_rate"
    container0.append(label_ret_backlog_rate, 'label_ret_backlog_rate')
    self.button_ret_order = Button()
    self.button_ret_order.attr_class = "Button"
    self.button_ret_order.attr_editor_newclass = False
    self.button_ret_order.css_background_color = "rgb(0,200,200)"
    self.button_ret_order.css_border_style = "none"
    self.button_ret_order.css_flex = "1"
    self.button_ret_order.css_font_family = "tahoma"
    self.button_ret_order.css_font_size = "16px"
    self.button_ret_order.css_height = "30.0px"
    self.button_ret_order.css_left = "200.0px"
    self.button_ret_order.css_position = "absolute"
    self.button_ret_order.css_top = "60.0px"
    self.button_ret_order.css_width = "100.0px"
    self.button_ret_order.text = "Order"
    self.button_ret_order.variable_name = "button_ret_order"
    self.button_ret_order.css_color = "rgb(255,255,255)"
    container0.append(self.button_ret_order, 'button_ret_order')
    self.label_ret_period = Label()
    self.label_ret_period.attr_class = "Label"
    self.label_ret_period.attr_editor_newclass = False
    self.label_ret_period.css_font_family = "Tahoma"
    self.label_ret_period.css_font_size = "22px"
    self.label_ret_period.css_font_style = "normal"
    self.label_ret_period.css_font_weight = "bold"
    self.label_ret_period.css_height = "30.0px"
    self.label_ret_period.css_left = "10.0px"
    self.label_ret_period.css_position = "absolute"
    self.label_ret_period.css_top = "10.0px"
    self.label_ret_period.css_width = "280.0px"
    self.label_ret_period.text = "Current Period: 0"
    self.label_ret_period.variable_name = "label_ret_period"
    container0.append(self.label_ret_period, 'label_ret_period')

    self.button_ret_order.set_enabled(False)
    self.button_ret_update.set_enabled(False)
    self.button_ret_order.css_background_color = "rgb(200,200,200)"
    self.button_ret_update.css_background_color = "rgb(200,200,200)"
    self.button_ret_disconnect.set_enabled(False)
    self.button_ret_disconnect.css_background_color = "rgb(200,200,200)"

    self.button_ret_connect.onclick.do(functools.partial(self.on_button_ret_connect_pressed, self.textEditPassRet,
                                                         self.textEditServerRet, self.textEditPortRet,
                                                         self.label_ret_info, self.button_ret_update,
                                                         self.button_ret_disconnect))

    self.button_ret_order.onclick.do(functools.partial(self.on_button_ret_place_order_pressed,
                                                       self.textEditOrderRetailer, self.textEditPortRet,
                                                       self.button_ret_order))

    self.button_ret_disconnect.onclick.do(functools.partial(self.on_button_ret_disconnect_pressed,
                                                            self.button_ret_connect, self.label_ret_info))

    self.button_ret_update.onclick.do(functools.partial(self.on_button_ret_update_pressed, self.button_ret_order,
                                                        self.label_ret_period, self.textEditPortRet, self.label_ret_costs,
                                                        self.label_ret_demand, self.label_ret_sl, self.label_ret_inventory,
                                                        self.label_ret_backlog, self.label_ret_status))

    return container0


def on_button_ret_connect_pressed(self, widget):
    widgets = [self.textEditPassRet, self.textEditServerRet, self.textEditPortRet, self.label_ret_info,
               self.button_ret_update, self.button_ret_disconnect]
    ret_remi_st.ret_remi.on_button_ret_connect_pressed(functools.partial(self, *widgets))


def on_button_ret_disconnect_pressed(self, widget):
    ret_remi_st.ret_remi.on_button_ret_disconnect_pressed(functools.partial(self, self.button_ret_connect,
                                                                            self.label_ret_info))


def on_button_ret_update_pressed(self, widget):
    widgets = [self.button_ret_order, self.label_ret_period, self.textEditPortRet, self.label_ret_costs,
               self.label_ret_demand, self.label_ret_sl, self.label_ret_inventory, self.label_ret_backlog, self.label_ret_status]
    ret_remi_st.ret_remi.on_button_ret_update_pressed(functools.partial(self, *widgets))


def on_button_ret_place_order_pressed(self, widget):
    ret_remi_st.ret_remi.on_button_ret_place_order_pressed(functools.partial(self, self.textEditOrderRetailer,
                                                                             self.textEditPortRet, self.button_ret_order))
