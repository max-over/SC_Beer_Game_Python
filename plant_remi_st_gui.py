from remi.gui import *
import plant_remi_st
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
    label_plant_ordersize = Label()
    label_plant_ordersize.attr_class = "Label"
    label_plant_ordersize.attr_editor_newclass = False
    label_plant_ordersize.css_font_family = "Tahoma"
    label_plant_ordersize.css_font_size = "18px"
    label_plant_ordersize.css_height = "30px"
    label_plant_ordersize.css_left = "10.0px"
    label_plant_ordersize.css_position = "absolute"
    label_plant_ordersize.css_top = "55.0px"
    label_plant_ordersize.css_width = "100px"
    label_plant_ordersize.text = "Order Size:"
    label_plant_ordersize.variable_name = "label_plant_ordersize"
    container0.append(label_plant_ordersize, 'label_plant_ordersize')
    label_plant_prodlot = Label()
    label_plant_prodlot.attr_class = "Label"
    label_plant_prodlot.attr_editor_newclass = False
    label_plant_prodlot.css_font_family = "Tahoma"
    label_plant_prodlot.css_font_size = "18px"
    label_plant_prodlot.css_height = "30px"
    label_plant_prodlot.css_left = "10.0px"
    label_plant_prodlot.css_position = "absolute"
    label_plant_prodlot.css_top = "95.0px"
    label_plant_prodlot.css_width = "100px"
    label_plant_prodlot.text = "Prod.lot:"
    label_plant_prodlot.variable_name = "label_plant_prodlot"
    container0.append(label_plant_prodlot, 'label_plant_prodlot')
    label_plant_shipment = Label()
    label_plant_shipment.attr_class = "Label"
    label_plant_shipment.attr_editor_newclass = False
    label_plant_shipment.css_font_family = "Tahoma"
    label_plant_shipment.css_font_size = "18px"
    label_plant_shipment.css_height = "30px"
    label_plant_shipment.css_left = "10.0px"
    label_plant_shipment.css_position = "absolute"
    label_plant_shipment.css_top = "135.0px"
    label_plant_shipment.css_width = "100px"
    label_plant_shipment.text = "Shipment:"
    label_plant_shipment.variable_name = "label_plant_shipment"
    container0.append(label_plant_shipment, 'label_plant_shipment')
    self.label_plant_period = Label()
    self.label_plant_period.attr_class = "Label"
    self.label_plant_period.attr_editor_newclass = False
    self.label_plant_period.css_font_family = "Tahoma"
    self.label_plant_period.css_font_size = "22px"
    self.label_plant_period.css_font_style = "normal"
    self.label_plant_period.css_font_weight = "bold"
    self.label_plant_period.css_height = "30.0px"
    self.label_plant_period.css_left = "10.0px"
    self.label_plant_period.css_position = "absolute"
    self.label_plant_period.css_top = "10.0px"
    self.label_plant_period.css_width = "280.0px"
    self.label_plant_period.text = "Current Period: 0"
    self.label_plant_period.variable_name = "label_plant_period"
    container0.append(self.label_plant_period, 'label_plant_period')
    self.textEditOrderPlant = TextInput()
    self.textEditOrderPlant.attr_class = "TextInput"
    self.textEditOrderPlant.attr_editor_newclass = False
    self.textEditOrderPlant.css_font_family = "tahoma"
    self.textEditOrderPlant.css_font_size = "20px"
    self.textEditOrderPlant.css_height = "30.0px"
    self.textEditOrderPlant.css_left = "110.0px"
    self.textEditOrderPlant.css_position = "absolute"
    self.textEditOrderPlant.css_text_align = "right"
    self.textEditOrderPlant.css_top = "60.0px"
    self.textEditOrderPlant.css_width = "75.0px"
    self.textEditOrderPlant.text = "1"
    self.textEditOrderPlant.variable_name = "textEditOrderPlant"
    container0.append(self.textEditOrderPlant, 'textEditOrderPlant')
    self.textEditProdlotPlant = TextInput()
    self.textEditProdlotPlant.attr_class = "TextInput"
    self.textEditProdlotPlant.attr_editor_newclass = False
    # textEditShipmentRetailer.attr_maxlength = "0"
    self.textEditProdlotPlant.css_font_family = "tahoma"
    self.textEditProdlotPlant.css_font_size = "20px"
    self.textEditProdlotPlant.css_height = "30.0px"
    self.textEditProdlotPlant.css_left = "110.0px"
    self.textEditProdlotPlant.css_position = "absolute"
    self.textEditProdlotPlant.css_text_align = "right"
    self.textEditProdlotPlant.css_top = "100.0px"
    self.textEditProdlotPlant.css_width = "75.0px"
    self.textEditProdlotPlant.text = "1"
    self.textEditProdlotPlant.variable_name = "textEditProdlotPlant"
    container0.append(self.textEditProdlotPlant, 'textEditProdlotPlant')
    self.textEditShipmentPlant = TextInput()
    self.textEditShipmentPlant.attr_class = "TextInput"
    self.textEditShipmentPlant.attr_editor_newclass = False
    self.textEditShipmentPlant.css_font_family = "tahoma"
    self.textEditShipmentPlant.css_font_size = "20px"
    self.textEditShipmentPlant.css_height = "30.0px"
    self.textEditShipmentPlant.css_left = "110.0px"
    self.textEditShipmentPlant.css_position = "absolute"
    self.textEditShipmentPlant.css_text_align = "right"
    self.textEditShipmentPlant.css_top = "140.0px"
    self.textEditShipmentPlant.css_width = "75.0px"
    self.textEditShipmentPlant.text = "1"
    self.textEditShipmentPlant.variable_name = "textEditShipmentPlant"
    container0.append(self.textEditShipmentPlant, 'textEditShipmentPlant')
    self.label_plant_info = Label()
    self.label_plant_info.attr_class = "Label"
    self.label_plant_info.attr_editor_newclass = False
    self.label_plant_info.css_height = "30.0px"
    self.label_plant_info.css_left = "10.0px"
    self.label_plant_info.css_position = "absolute"
    self.label_plant_info.css_top = "555.0px"
    self.label_plant_info.text = "Info"
    self.label_plant_info.css_visibility = "hidden"
    self.label_plant_info.variable_name = "label_plant_info"
    self.label_plant_info.css_width = "300.0px"
    self.label_plant_info.css_font_family = "tahoma"
    self.label_plant_info.css_font_size = "12px"
    container0.append(self.label_plant_info, 'label_plant_info')
    label_plant_server = Label()
    label_plant_server.attr_class = "Label"
    label_plant_server.attr_editor_newclass = False
    label_plant_server.css_height = "30.0px"
    label_plant_server.css_left = "10.0px"
    label_plant_server.css_position = "absolute"
    label_plant_server.css_top = "465.0px"
    label_plant_server.css_width = "60.0px"
    label_plant_server.text = "Server:"
    label_plant_server.variable_name = "label_plant_server"
    container0.append(label_plant_server, 'label_plant_server')
    label_plant_pass = Label()
    label_plant_pass.attr_class = "Label"
    label_plant_pass.attr_editor_newclass = False
    label_plant_pass.css_height = "30.0px"
    label_plant_pass.css_left = "10.0px"
    label_plant_pass.css_position = "absolute"
    label_plant_pass.css_top = "425.0px"
    label_plant_pass.css_width = "60.0px"
    label_plant_pass.text = "Password:"
    label_plant_pass.css_font_family = "Tahoma"
    label_plant_pass.css_font_size = "14px"
    label_plant_pass.variable_name = "label_plant_pass"
    container0.append(label_plant_pass, 'label_plant_pass')
    label_plant_port = Label()
    label_plant_port.attr_class = "Label"
    label_plant_port.attr_editor_newclass = False
    label_plant_port.css_height = "30.0px"
    label_plant_port.css_left = "10.0px"
    label_plant_port.css_position = "absolute"
    label_plant_port.css_top = "510.0px"
    label_plant_port.css_width = "45.0px"
    label_plant_port.text = "Port:"
    label_plant_port.variable_name = "label_plant_port"
    container0.append(label_plant_port, 'label_plant_port')
    self.textEditServerPlant = TextInput()
    self.textEditServerPlant.attr_class = "TextInput"
    self.textEditServerPlant.attr_editor_newclass = False
    self.textEditServerPlant.css_font_family = "Tahoma"
    self.textEditServerPlant.css_height = "30.0px"
    self.textEditServerPlant.css_left = "75.0px"
    self.textEditServerPlant.css_position = "absolute"
    self.textEditServerPlant.css_text_align = "center"
    self.textEditServerPlant.css_top = "465.0px"
    self.textEditServerPlant.css_width = "225.0px"
    self.textEditServerPlant.text = "localhost"
    self.textEditServerPlant.variable_name = "textEditServerPlant"
    container0.append(self.textEditServerPlant, 'textEditServerPlant')
    self.textEditPassPlant = TextInput()
    self.textEditPassPlant.attr_class = "TextInput"
    self.textEditPassPlant.attr_editor_newclass = False
    self.textEditPassPlant.css_font_family = "Tahoma"
    self.textEditPassPlant.css_height = "30.0px"
    self.textEditPassPlant.css_left = "75.0px"
    self.textEditPassPlant.css_position = "absolute"
    self.textEditPassPlant.css_top = "425.0px"
    self.textEditPassPlant.css_width = "225.0px"
    self.textEditPassPlant.text = "passphrase"
    self.textEditPassPlant.css_text_align = "center"
    self.textEditPassPlant.variable_name = "textEditPassPlant"
    container0.append(self.textEditPassPlant, 'textEditPassPlant')
    self.textEditPortPlant = TextInput()
    self.textEditPortPlant.attr_class = "TextInput"
    self.textEditPortPlant.attr_editor_newclass = False
    self.textEditPortPlant.css_align_self = "center"
    self.textEditPortPlant.css_font_family = "Tahoma"
    self.textEditPortPlant.css_height = "40.0px"
    self.textEditPortPlant.css_left = "75.0px"
    self.textEditPortPlant.css_position = "absolute"
    self.textEditPortPlant.css_text_align = "center"
    self.textEditPortPlant.css_top = "510.0px"
    self.textEditPortPlant.css_width = "120.0px"
    self.textEditPortPlant.text = "5555"
    self.textEditPortPlant.variable_name = "textEditPortPlant"
    container0.append(self.textEditPortPlant, 'textEditPortPlant')
    self.button_plant_connect = Button()
    self.button_plant_connect.attr_class = "Button"
    self.button_plant_connect.css_border_style = "none"
    self.button_plant_connect.attr_editor_newclass = False
    self.button_plant_connect.css_background_color = "rgb(184,184,105)"
    self.button_plant_connect.css_font_family = "Tahoma"
    self.button_plant_connect.css_font_size = "16px"
    self.button_plant_connect.css_height = "40.0px"
    self.button_plant_connect.css_left = "210.0px"
    self.button_plant_connect.css_position = "absolute"
    self.button_plant_connect.css_top = "510.0px"
    self.button_plant_connect.css_width = "90.0px"
    self.button_plant_connect.text = "Connect"
    self.button_plant_connect.css_color = "rgb(255,255,255)"
    self.button_plant_connect.variable_name = "button_plant_connect"
    container0.append(self.button_plant_connect, 'button_plant_connect')
    self.button_plant_disconnect = Button()
    self.button_plant_disconnect.attr_class = "Button"
    self.button_plant_disconnect.css_border_style = "none"
    self.button_plant_disconnect.attr_editor_newclass = False
    self.button_plant_disconnect.css_background_color = "rgb(184,184,105)"
    self.button_plant_disconnect.css_font_family = "Tahoma"
    self.button_plant_disconnect.css_font_size = "16px"
    self.button_plant_disconnect.css_height = "40.0px"
    self.button_plant_disconnect.css_left = "690.0px"
    self.button_plant_disconnect.css_position = "absolute"
    self.button_plant_disconnect.css_top = "510.0px"
    self.button_plant_disconnect.css_width = "100.0px"
    self.button_plant_disconnect.text = "Disconnect"
    self.button_plant_disconnect.css_color = "rgb(255,255,255)"
    self.button_plant_disconnect.variable_name = "button_plant_disconnect"
    container0.append(self.button_plant_disconnect, 'button_plant_disconnect')
    self.button_plant_update = Button()
    self.button_plant_update.attr_class = "Button"
    self.button_plant_update.css_border_style = "none"
    self.button_plant_update.attr_editor_newclass = False
    self.button_plant_update.css_background_color = "rgb(184,184,105)"
    self.button_plant_update.css_font_family = "Tahoma"
    self.button_plant_update.css_font_size = "16px"
    self.button_plant_update.css_height = "40.0px"
    self.button_plant_update.css_left = "10.0px"
    self.button_plant_update.css_position = "absolute"
    self.button_plant_update.css_top = "190.0px"
    self.button_plant_update.css_width = "100.0px"
    self.button_plant_update.text = "Update"
    self.button_plant_update.css_color = "rgb(255,255,255)"
    self.button_plant_update.variable_name = "button_plant_update"
    container0.append(self.button_plant_update, 'button_plant_update')
    label_plant_turnstatus = Label()
    label_plant_turnstatus.attr_class = "Label"
    label_plant_turnstatus.attr_editor_newclass = False
    label_plant_turnstatus.css_font_family = "Tahoma"
    label_plant_turnstatus.css_font_size = "22px"
    label_plant_turnstatus.css_font_weight = "bold"
    label_plant_turnstatus.css_height = "40.0px"
    label_plant_turnstatus.css_left = "520.0px"
    label_plant_turnstatus.css_position = "absolute"
    label_plant_turnstatus.css_top = "10.0px"
    label_plant_turnstatus.css_width = "160.0px"
    label_plant_turnstatus.text = "Turn Status"
    label_plant_turnstatus.variable_name = "label_plant_turnstatus"
    container0.append(label_plant_turnstatus, 'label_plant_turnstatus')
    label_plant_leadtime = Label()
    label_plant_leadtime.attr_class = "Label"
    label_plant_leadtime.attr_editor_newclass = False
    label_plant_leadtime.css_font_family = "tahoma"
    label_plant_leadtime.css_font_size = "14px"
    label_plant_leadtime.css_font_weight = "bold"
    label_plant_leadtime.css_height = "30.0px"
    label_plant_leadtime.css_left = "320.0px"
    label_plant_leadtime.css_position = "absolute"
    label_plant_leadtime.css_top = "50.0px"
    label_plant_leadtime.css_width = "190.0px"
    label_plant_leadtime.set_text("Leadtime to Supplier: " + str(plant_remi_st.LEADTIMEUP))
    label_plant_leadtime.variable_name = "label_plant_leadtime"
    container0.append(label_plant_leadtime, 'label_plant_leadtime')
    self.label_plant_status = Label()
    self.label_plant_status.attr_class = "Label"
    self.label_plant_status.attr_editor_newclass = False
    self.label_plant_status.css_font_family = "tahoma"
    self.label_plant_status.css_font_size = "14px"
    self.label_plant_status.css_height = "260.0px"
    self.label_plant_status.css_left = "520.0px"
    self.label_plant_status.css_position = "absolute"
    self.label_plant_status.css_top = "50.0px"
    self.label_plant_status.css_white_space = "pre-wrap"
    self.label_plant_status.css_width = "270.0px"
    self.label_plant_status.text = "Turn status info"
    self.label_plant_status.variable_name = "label_plant_status"
    container0.append(self.label_plant_status, 'label_plant_status')
    label_plant_intransit = Label()
    label_plant_intransit.attr_class = "Label"
    label_plant_intransit.attr_editor_newclass = False
    label_plant_intransit.css_font_family = "tahoma"
    label_plant_intransit.css_font_size = "14px"
    label_plant_intransit.css_font_weight = "bold"
    label_plant_intransit.css_height = "30.0px"
    label_plant_intransit.css_left = "320.0px"
    label_plant_intransit.css_position = "absolute"
    label_plant_intransit.css_top = "10.0px"
    label_plant_intransit.css_width = "130.0px"
    label_plant_intransit.text = "In transit:"
    label_plant_intransit.variable_name = "label_plant_intransit"
    label_plant_intransit.css_visibility = "hidden"
    container0.append(label_plant_intransit, 'label_plant_intransit')
    self.label_plant_backlog = Label()
    self.label_plant_backlog.attr_class = "Label"
    self.label_plant_backlog.attr_editor_newclass = False
    self.label_plant_backlog.css_font_family = "tahoma"
    self.label_plant_backlog.css_font_size = "14px"
    self.label_plant_backlog.css_font_weight = "bold"
    self.label_plant_backlog.css_height = "30.0px"
    self.label_plant_backlog.css_left = "320.0px"
    self.label_plant_backlog.css_position = "absolute"
    self.label_plant_backlog.css_top = "90.0px"
    self.label_plant_backlog.css_width = "190.0px"
    self.label_plant_backlog.text = "Backlog (total):"
    self.label_plant_backlog.variable_name = "label_plant_backlog"
    container0.append(self.label_plant_backlog, 'label_plant_backlog')
    self.label_plant_inventory_raw = Label()
    self.label_plant_inventory_raw.attr_class = "Label"
    self.label_plant_inventory_raw.attr_editor_newclass = False
    self.label_plant_inventory_raw.css_font_family = "tahoma"
    self.label_plant_inventory_raw.css_font_size = "14px"
    self.label_plant_inventory_raw.css_font_weight = "bold"
    self.label_plant_inventory_raw.css_height = "30.0px"
    self.label_plant_inventory_raw.css_left = "320.0px"
    self.label_plant_inventory_raw.css_position = "absolute"
    self.label_plant_inventory_raw.css_top = "130.0px"
    self.label_plant_inventory_raw.css_width = "190.0px"
    self.label_plant_inventory_raw.text = "Inventory raw:"
    self.label_plant_inventory_raw.variable_name = "label_plant_inventory_raw"
    container0.append(self.label_plant_inventory_raw, 'label_plant_inventory_raw')
    self.label_plant_inventory_finished = Label()
    self.label_plant_inventory_finished.attr_class = "Label"
    self.label_plant_inventory_finished.attr_editor_newclass = False
    self.label_plant_inventory_finished.css_font_family = "tahoma"
    self.label_plant_inventory_finished.css_font_size = "14px"
    self.label_plant_inventory_finished.css_font_weight = "bold"
    self.label_plant_inventory_finished.css_height = "30.0px"
    self.label_plant_inventory_finished.css_left = "320.0px"
    self.label_plant_inventory_finished.css_position = "absolute"
    self.label_plant_inventory_finished.css_top = "170.0px"
    self.label_plant_inventory_finished.css_width = "190.0px"
    self.label_plant_inventory_finished.text = "Inventory finished:"
    self.label_plant_inventory_finished.variable_name = "label_plant_inventory_finished"
    container0.append(self.label_plant_inventory_finished, 'label_plant_inventory_finished')
    self.label_plant_demand = Label()
    self.label_plant_demand.attr_class = "Label"
    self.label_plant_demand.attr_editor_newclass = False
    self.label_plant_demand.css_font_family = "tahoma"
    self.label_plant_demand.css_font_size = "14px"
    self.label_plant_demand.css_font_weight = "bold"
    self.label_plant_demand.css_height = "30.0px"
    self.label_plant_demand.css_left = "320.0px"
    self.label_plant_demand.css_position = "absolute"
    self.label_plant_demand.css_top = "210.0px"
    self.label_plant_demand.css_width = "190.0px"
    self.label_plant_demand.text = "Demand:"
    self.label_plant_demand.variable_name = "label_plant_demand"
    container0.append(self.label_plant_demand, 'label_plant_demand')
    self.label_plant_costs = Label()
    self.label_plant_costs.attr_class = "Label"
    self.label_plant_costs.attr_editor_newclass = False
    self.label_plant_costs.css_font_family = "tahoma"
    self.label_plant_costs.css_font_size = "18px"
    self.label_plant_costs.css_height = "30.0px"
    self.label_plant_costs.css_left = "10.0px"
    self.label_plant_costs.css_position = "absolute"
    self.label_plant_costs.css_top = "240.0px"
    self.label_plant_costs.css_width = "290.0px"
    self.label_plant_costs.text = "Costs (total):"
    self.label_plant_costs.variable_name = "label_plant_costs"
    container0.append(self.label_plant_costs, 'label_plant_costs')
    self.label_plant_sl = Label()
    self.label_plant_sl.attr_class = "Label"
    self.label_plant_sl.attr_editor_newclass = False
    self.label_plant_sl.css_font_family = "tahoma"
    self.label_plant_sl.css_font_size = "18px"
    self.label_plant_sl.css_height = "30.0px"
    self.label_plant_sl.css_left = "10.0px"
    self.label_plant_sl.css_position = "absolute"
    self.label_plant_sl.css_top = "280.0px"
    self.label_plant_sl.css_width = "290.0px"
    self.label_plant_sl.text = "SL:"
    self.label_plant_sl.variable_name = "label_plant_sl"
    container0.append(self.label_plant_sl, 'label_plant_sl')
    label_plant_holding_raw_rate = Label()
    label_plant_holding_raw_rate.attr_class = "Label"
    label_plant_holding_raw_rate.attr_editor_newclass = False
    label_plant_holding_raw_rate.css_font_family = "tahoma"
    label_plant_holding_raw_rate.css_font_size = "12px"
    label_plant_holding_raw_rate.css_height = "25.0px"
    label_plant_holding_raw_rate.css_left = "520px"
    label_plant_holding_raw_rate.css_position = "absolute"
    label_plant_holding_raw_rate.css_top = "275.0px"
    label_plant_holding_raw_rate.css_width = "270px"
    label_plant_holding_raw_rate.set_text("Holding raw costs rate: " + str(plant_remi_st.HOLDINGRATE_RAW))
    label_plant_holding_raw_rate.variable_name = "label_plant_holding_raw_rate"
    container0.append(label_plant_holding_raw_rate, 'label_plant_holding_raw_rate')
    label_plant_backlog_rate = Label()
    label_plant_backlog_rate.attr_class = "Label"
    label_plant_backlog_rate.attr_editor_newclass = False
    label_plant_backlog_rate.css_font_family = "tahoma"
    label_plant_backlog_rate.css_font_size = "12px"
    label_plant_backlog_rate.css_height = "25.0px"
    label_plant_backlog_rate.css_left = "520.0px"
    label_plant_backlog_rate.css_position = "absolute"
    label_plant_backlog_rate.css_top = "335.0px"
    label_plant_backlog_rate.css_width = "270.0px"
    label_plant_backlog_rate.set_text("Backlog costs rate: " + str(plant_remi_st.BACKLOGRATE))
    label_plant_backlog_rate.variable_name = "label_plant_backlog_rate"
    container0.append(label_plant_backlog_rate, 'label_plant_backlog_rate')
    label_plant_holding_fg_rate = Label()
    label_plant_holding_fg_rate.attr_class = "Label"
    label_plant_holding_fg_rate.attr_editor_newclass = False
    label_plant_holding_fg_rate.css_font_family = "tahoma"
    label_plant_holding_fg_rate.css_font_size = "12px"
    label_plant_holding_fg_rate.css_height = "25.0px"
    label_plant_holding_fg_rate.css_left = "520.0px"
    label_plant_holding_fg_rate.css_position = "absolute"
    label_plant_holding_fg_rate.css_top = "305.0px"
    label_plant_holding_fg_rate.css_width = "270px"
    label_plant_holding_fg_rate.set_text("Holding FG costs rate: " + str(plant_remi_st.HOLDINGRATE_FINISHED))
    label_plant_holding_fg_rate.variable_name = "label_plant_holding_fg_rate"
    container0.append(label_plant_holding_fg_rate, 'label_plant_holding_fg_rate')
    self.button_plant_order = Button()
    self.button_plant_order.attr_class = "Button"
    self.button_plant_order.attr_editor_newclass = False
    self.button_plant_order.css_background_color = "rgb(184,184,105)"
    self.button_plant_order.css_border_style = "none"
    self.button_plant_order.css_flex = "1"
    self.button_plant_order.css_font_family = "Tahoma"
    self.button_plant_order.css_font_size = "16px"
    self.button_plant_order.css_height = "30.0px"
    self.button_plant_order.css_left = "200.0px"
    self.button_plant_order.css_position = "absolute"
    self.button_plant_order.css_top = "60.0px"
    self.button_plant_order.css_width = "100.0px"
    self.button_plant_order.text = "Order"
    self.button_plant_order.css_color = "rgb(255,255,255)"
    self.button_plant_order.variable_name = "button_plant_order"
    container0.append(self.button_plant_order, 'button_plant_order')
    self.button_plant_produce = Button()
    self.button_plant_produce.attr_class = "Button"
    self.button_plant_produce.attr_editor_newclass = False
    self.button_plant_produce.css_background_color = "rgb(184,184,105)"
    self.button_plant_produce.css_border_style = "none"
    self.button_plant_produce.css_flex = "1"
    self.button_plant_produce.css_font_family = "Tahoma"
    self.button_plant_produce.css_font_size = "16px"
    self.button_plant_produce.css_height = "30.0px"
    self.button_plant_produce.css_left = "200.0px"
    self.button_plant_produce.css_position = "absolute"
    self.button_plant_produce.css_top = "100.0px"
    self.button_plant_produce.css_width = "100.0px"
    self.button_plant_produce.text = "Produce"
    self.button_plant_produce.css_color = "rgb(255,255,255)"
    self.button_plant_produce.variable_name = "button_plant_produce"
    container0.append(self.button_plant_produce, 'button_plant_produce')
    self.button_plant_shipment = Button()
    self.button_plant_shipment.attr_class = "Button"
    self.button_plant_shipment.attr_editor_newclass = False
    self.button_plant_shipment.css_background_color = "rgb(184,184,105)"
    self.button_plant_shipment.css_border_style = "none"
    self.button_plant_shipment.css_flex = "1"
    self.button_plant_shipment.css_font_family = "Tahoma"
    self.button_plant_shipment.css_font_size = "16px"
    self.button_plant_shipment.css_height = "30.0px"
    self.button_plant_shipment.css_left = "200.0px"
    self.button_plant_shipment.css_position = "absolute"
    self.button_plant_shipment.css_top = "140.0px"
    self.button_plant_shipment.css_width = "100.0px"
    self.button_plant_shipment.text = "Shipment"
    self.button_plant_shipment.css_color = "rgb(255,255,255)"
    self.button_plant_shipment.variable_name = "button_plant_shipment"
    container0.append(self.button_plant_shipment, 'button_plant_shipment')

    self.button_plant_order.set_enabled(0)
    self.button_plant_update.set_enabled(0)
    self.button_plant_shipment.set_enabled(0)
    self.button_plant_produce.set_enabled(0)
    self.button_plant_order.css_background_color = "rgb(200,200,200)"
    self.button_plant_update.css_background_color = "rgb(200,200,200)"
    self.button_plant_shipment.css_background_color = "rgb(200,200,200)"
    self.button_plant_produce.css_background_color = "rgb(200,200,200)"
    self.button_plant_disconnect.set_enabled(0)
    self.button_plant_disconnect.css_background_color = "rgb(200,200,200)"

    self.button_plant_connect.onclick.do(functools.partial(self.on_button_plant_connect_pressed, self.textEditPassPlant,
                                                           self.textEditServerPlant, self.textEditPortPlant,
                                                           self.label_plant_info, self.button_plant_update,
                                                           self.button_plant_disconnect))
    self.button_plant_disconnect.onclick.do(functools.partial(self.on_button_plant_disconnect_pressed,
                                                              self.button_plant_connect, self.label_plant_info))
    self.button_plant_update.onclick.do(functools.partial(self.on_button_plant_update_pressed,self.label_plant_demand,
                                                          self.button_plant_shipment, self.label_plant_period,
                                                          self.textEditPortPlant, self.label_plant_costs,
                                                          self.label_plant_inventory_finished, self.label_plant_inventory_raw,
                                                          self.label_plant_backlog, self.label_plant_status))
    self.button_plant_shipment.onclick.do(functools.partial(self.on_button_plant_shipment_pressed,
                                                            self.textEditShipmentPlant, self.label_plant_sl,
                                                            self.textEditPortPlant,self.label_plant_inventory_finished,
                                                            self.label_plant_backlog, self.button_plant_shipment,
                                                            self.button_plant_produce))
    self.button_plant_order.onclick.do(functools.partial(self.on_button_plant_order_pressed, self.textEditOrderPlant,
                                                         self.button_plant_order, self.textEditPortPlant))
    self.button_plant_produce.onclick.do(functools.partial(self.on_button_plant_produce_pressed,
                                                           self.textEditProdlotPlant, self.label_plant_inventory_raw,
                                                           self.button_plant_order,self.button_plant_produce))

    return container0

def on_button_plant_disconnect_pressed(self, widget):
    plant_remi_st.plant_remi.on_button_plant_disconnect_pressed(functools.partial(self, self.button_plant_connect,
                                                                                  self.label_plant_info))

def on_button_plant_produce_pressed(self, widget):
    on_button_plant_produce_pressed(functools.partial(self, self.textEditProdlotPlant, self.label_plant_inventory_raw,
                                                      self.button_plant_order, self.button_plant_produce))

def on_button_plant_connect_pressed(self, widget):
    widgets = [self.textEditPassPlant, self.textEditServerPlant, self.textEditPortPlant, self.label_plant_info,
               self.button_plant_update, self.button_plant_disconnect]
    plant_remi_st.plant_remi.on_button_plant_connect_pressed(functools.partial(self, *widgets))

def on_button_plant_update_pressed(self, widget):
    widgets = [self.label_plant_demand, self.button_plant_shipment, self.label_plant_period, self.textEditPortPlant,
               self.label_plant_costs, self.label_plant_inventory_finished, self.label_plant_inventory_raw,
               self.label_plant_backlog, self.label_plant_status]
    plant_remi_st.plant_remi.on_button_plant_update_pressed(functools.partial(self, *widgets))

def on_button_plant_shipment_pressed(self, widget):
    widgets = [self.textEditShipmentPlant, self.label_plant_sl, self.textEditPortPlant,self.label_plant_inventory_finished,
               self.label_plant_backlog, self.button_plant_shipment, self.button_plant_produce]
    plant_remi_st.plant_remi.on_button_plant_shipment_pressed(functools.partial(self, *widgets))

def on_button_plant_order_pressed(self, widget):
    plant_remi_st.plant_remi.on_button_plant_order_pressed(functools.partial(self, textEditOrderPlant,
                                                                             button_plant_order, textEditPortPlant))