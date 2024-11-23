import socket
import threading
import pickle
import time
from xlwt import Workbook

xtime = str(round(time.time()))


class ProcessData:
    def __init__(self, data_id, data_list, data_leadtimeup):
        self.data_id = data_id
        self.data_list = data_list
        self.data_leadtimeup = data_leadtimeup


HOST = ""
PORT = 5555

wb = Workbook()

sheet_ret = wb.add_sheet("Retailer")
sheet_ret.write(0, 0, "Period")
sheet_ret.write(0, 1, "Demand")
sheet_ret.write(0, 2, "Order")
sheet_ret.write(0, 3, "Shipment")
sheet_distr = wb.add_sheet("Distributor")
sheet_distr.write(0, 0, "Period")
sheet_distr.write(0, 1, "Demand")
sheet_distr.write(0, 2, "Order")
sheet_distr.write(0, 3, "Shipment")
sheet_whole = wb.add_sheet("Wholesaler")
sheet_whole.write(0, 0, "Period")
sheet_whole.write(0, 1, "Demand")
sheet_whole.write(0, 2, "Order")
sheet_whole.write(0, 3, "Shipment")
sheet_plant = wb.add_sheet("Plant")
sheet_plant.write(0, 0, "Period")
sheet_plant.write(0, 1, "Demand")
sheet_plant.write(0, 2, "Order")
sheet_plant.write(0, 3, "Production")
sheet_plant.write(0, 4, "Shipment")


class SocketServer:
    def __init__(self, host, port):
        self.connected_clients = []
        self.host = host
        self.port = port
        self.connected = set()
        self.games = {}
        self.idCount = 0
        self.dataCount = 0
        self.ret_order = 0
        self.distr_order = 0
        self.whole_order = 0
        self.currentPeriod = 0
        self.currentDemand = 0
        self.distrShipmentPlaced = 0
        self.distrShipment = 0
        self.wholeShipmentPlaced = 0
        self.wholeShipment = 0
        self.plantShipmentPlaced = 0
        self.plantShipment = 0
        self.plantProdlotPlaced = 0
        self.plantProdlot = 0
        self.plant_order = 0
        self.supplShipmentPlaced = 0
        self.shipment_ret_queue = []
        self.shipment_distr_queue = []
        self.shipment_whole_queue = []
        self.shipment_plant_queue = []
        self.production_plant_queue = []
        self.prodshipmentList = []
        self.ret_inventorycosts = 0
        self.ret_inventory = 0
        self.ret_backlogcosts = 0
        self.ret_backlogtotal = 0
        self.ret_costs = 0
        self.ret_lastperiod = 0
        self.distr_inventorycosts = 0
        self.distr_inventory = 0
        self.distr_backlogcosts = 0
        self.distr_backlogtotal = 0
        self.distr_costs = 0
        self.distr_lastperiod = 0
        self.whole_inventorycosts = 0
        self.whole_inventory = 0
        self.whole_backlogcosts = 0
        self.whole_backlogtotal = 0
        self.whole_costs = 0
        self.whole_lastperiod = 0
        self.plant_inventorycosts = 0
        self.plant_inventory_raw = 0
        self.plant_inventory_finished = 0
        self.plant_backlogcosts = 0
        self.plant_backlogtotal = 0
        self.plant_costs = 0
        self.plant_lastperiod = 0
        self.supplier_order = 0

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(4)
        self.handlers = {}
        print("Waiting for a connection, Server Started")

    def accept_connections(self):
        while True:
            client, address = self.server.accept()
            self.idCount += 1
            p = self.idCount
            self.connected_clients.append(client)
            client_thread = threading.Thread(target=self.handle_client, args=(client, address, p))
            client_thread.start()

    def register_handler(self, command, handler):
        self.handlers[command] = handler

    def handle_client(self, client, address, p):
        print(f"Accepted connection from {address}")
        client.send(str.encode(str(p)))
        self.dataCount += 1
        while True:
            try:
                data = pickle.loads(client.recv(40960))
                if not data:
                    break
                elif data.data_id in self.handlers:
                    self.handlers[data.data_id](client, data)
                else:
                    client.sendall(pickle.dumps(""))
                    print("Player disconnected")
                    client.close()
                    break
            except ConnectionError:
                error_message = "Error: Connection lost"
                print(f"{address} disconnected: {error_message}")
                client.close()
                break
        self.idCount -= 1
        client.close()

    def handle_get_adm(self, client, data):
        print("Administrator connected")
        self.xtime = str(round(time.time()))
        client.sendall(pickle.dumps(str(self.server)))

    def handle_get_ret(self, client, data):
        print("Retailer connected")
        client.sendall(pickle.dumps(str(self.server)))

    def handle_get_distr(self, client, data):
        print("Distributor connected")
        client.sendall(pickle.dumps(str(self.server)))

    def handle_get_whole(self, client, data):
        print("Wholesaler connected")
        client.sendall(pickle.dumps(str(self.server)))

    def handle_get_plant(self, client, data):
        print("Plant connected")
        client.sendall(pickle.dumps(str(self.server)))

    def handle_check_status(self, client, data):
        status = (f"Retailer: Order: {self.ret_order}\n"
                  f"Distr: Order: {self.distr_order} Shipment: {self.distrShipment}\n"
                  f"Whole: Order: {self.whole_order} Shipment: {self.wholeShipment}\n"
                  f"Plant: Order: {self.plant_order} Shipment: {self.plantShipment}")
        client.sendall(pickle.dumps(status))

    def handle_check_status_node(self, client, data):
        ret_placed = "placed" if str(self.ret_order) !="" else "no"
        distr_placed = "placed" if str(self.distr_order) !="" else "no"
        whole_placed = "placed" if str(self.whole_order) != "" else "no"
        plant_placed = "placed" if str(self.plant_order) != "" else "no"
        status = (f"Retailer: Order: {ret_placed}\n"
                  f"Distr: Order: {distr_placed} \n"
                  f"Whole: Order: {whole_placed} \n"
                  f"Plant: Order: {plant_placed} ")
        client.sendall(pickle.dumps(status))

    def handle_ret_order(self, client, data):
        self.ret_order = data.data_leadtimeup
        print("ret order: " + str(self.ret_order))
        sheet_ret.write(int(self.currentPeriod), 2, int(self.ret_order))
        sheet_distr.write(int(self.currentPeriod), 1, int(self.ret_order))
        wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_distr_order(self, client, data):
        self.distr_order = data.data_leadtimeup
        print("distr order: " + str(self.distr_order))
        sheet_distr.write(int(self.currentPeriod), 2, int(self.distr_order))
        sheet_whole.write(int(self.currentPeriod), 1, int(self.distr_order))
        wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_whole_order(self, client, data):
        self.whole_order = data.data_leadtimeup
        print("whole order: " + str(self.whole_order))
        sheet_whole.write(int(self.currentPeriod), 2, int(self.whole_order))
        sheet_plant.write(int(self.currentPeriod), 1, int(self.whole_order))
        wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))


    def handle_plant_order(self, client, data):
        if not self.supplShipmentPlaced:
            self.supplShipmentPlaced = 1
            self.plant_order = data.data_list
            print(f"plant order: {self.plant_order}")
            self.shipment_plant_queue.append((self.plant_order, data.data_leadtimeup))
            sheet_plant.write(int(self.currentPeriod), 2, int(self.plant_order))
            wb.save(f'xlwt_example{self.port}_{xtime}.xls')

        client.sendall(pickle.dumps(""))

    def handle_upd_ret_cust_demand(self, client, data):
        print("retailer update")
        client.sendall(pickle.dumps(ProcessData("", [0], self.currentDemand)))

    def handle_upd_ret_distr_demand(self, client, data):
        print("distributor update")
        client.sendall(pickle.dumps(ProcessData("", [0], self.ret_order)))

    def handle_upd_distr_whole_demand(self, client, data):
        print("wholesaler update")
        client.sendall(pickle.dumps(ProcessData("", [0], self.distr_order)))

    def handle_upd_whole_plant_demand(self, client, data):
        print("plant update")
        client.sendall(pickle.dumps(ProcessData("", [0], self.whole_order)))

    def handle_distr_shipment(self, client, data):
        if not self.distrShipmentPlaced:
            self.distrShipmentPlaced = 1
            self.distrShipment = data.data_leadtimeup
            print(f"distr shipment: {self.distrShipment}")
            self.shipment_ret_queue.append((self.distrShipment, self.currentPeriod))
            sheet_distr.write(int(self.currentPeriod), 3, int(self.distrShipment))
            wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_whole_shipment(self, client, data):
        if not self.wholeShipmentPlaced:
            self.wholeShipmentPlaced = 1
            self.wholeShipment = data.data_leadtimeup
            print(f"whole shipment: {self.wholeShipment}")
            self.shipment_distr_queue.append((self.wholeShipment, self.currentPeriod))
            sheet_whole.write(int(self.currentPeriod), 3, int(self.wholeShipment))
            wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_plant_shipment(self, client, data):
        if not self.plantShipmentPlaced:
            self.plantShipmentPlaced = 1
            self.plantShipment = data.data_leadtimeup
            print(f"plant shipment: {self.plantShipment}")
            self.shipment_whole_queue.append((self.plantShipment, self.currentPeriod))
            sheet_plant.write(int(self.currentPeriod), 4, int(self.plantShipment))
            wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_plant_prodlot(self, client, data):
        if not self.plantProdlotPlaced:
            self.plantProdlotPlaced = 1
            self.plantProdlot = data.data_list
            print(f"plant prodlot: {self.plantProdlot}")
            self.production_plant_queue.append((self.plantProdlot, data.data_leadtimeup))
            sheet_plant.write(int(self.currentPeriod), 3, int(self.plantProdlot))
            wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_distr_shipment(self, client, data):
        for row, (shipment, period) in enumerate(self.shipment_ret_queue):
            if int(period) == int(self.currentPeriod) - data.data_leadtimeup:
                cz = shipment
                break
        else:
            cz = ""
        if len(self.shipment_ret_queue) > 20:
            self.shipment_ret_queue.pop(0)
        client.sendall(pickle.dumps(ProcessData("", cz, 0)))

    def handle_upd_distr_whole_shipment(self, client, data):
        for row, (shipment, period) in enumerate(self.shipment_distr_queue):
            if int(period) == int(self.currentPeriod) - data.data_leadtimeup:
                cz = shipment
                break
        else:
            cz = ""
        if len(self.shipment_distr_queue) > 20:
            self.shipment_distr_queue.pop(0)
        client.sendall(pickle.dumps(ProcessData("", cz, 0)))

    def handle_upd_whole_plant_shipment(self, client, data):
        for row, (shipment, period) in enumerate(self.shipment_whole_queue):
            if int(period) == int(self.currentPeriod) - data.data_leadtimeup:
                cz = shipment
                break
        else:
            cz = ""
        if len(self.shipment_whole_queue) > 20:
            self.shipment_whole_queue.pop(0)
        client.sendall(pickle.dumps(ProcessData("", cz, 0)))

    def handle_upd_plant_suppl_shipment(self, client, data):
        for row, (shipment, period) in enumerate(self.shipment_plant_queue):
            if int(period) == int(self.currentPeriod):
                cz = shipment
                print(f"supplier shipment: {shipment}")
                break
        else:
            cz = ""
        if len(self.shipment_plant_queue) > 20:
            self.shipment_plant_queue.pop(0)
        client.sendall(pickle.dumps(ProcessData("", cz, 0)))

    def handle_upd_plant_produce_shipment(self, client, data):
        for row, (production, period) in enumerate(self.production_plant_queue):
            if int(period) == int(self.currentPeriod):
                cz = production
                break
        else:
            cz = ""
        if len(self.production_plant_queue) > 20:
            self.production_plant_queue.pop(0)
        client.sendall(pickle.dumps(ProcessData("", cz, 0)))

    def handle_add_status_ret(self, client, data):
        client.sendall(pickle.dumps(str(self.shipment_ret_queue)))

    def handle_add_status_distr(self, client, data):
        client.sendall(pickle.dumps(str(self.shipment_distr_queue)))

    def handle_add_status_whole(self, client, data):
        client.sendall(pickle.dumps(str(self.shipment_whole_queue)))

    def handle_disconnect(self, client, data):
        client.sendall(pickle.dumps(""))
        client.close()

    def handle_set_demand(self, client, data):
        self.currentDemand = data.data_leadtimeup
        print("Set demand: " + self.currentDemand)
        sheet_ret.write(int(self.currentPeriod), 1, int(self.currentDemand))
        wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_set_period(self, client, data):
        print("Set period: " + str(data.data_leadtimeup))
        self.currentPeriod = data.data_leadtimeup
        self.distrShipmentPlaced = 0
        self.wholeShipmentPlaced = 0
        self.plantShipmentPlaced = 0
        self.plantProdlotPlaced = 0
        self.supplShipmentPlaced = 0
        self.ret_order = ""
        self.distr_order = ""
        self.whole_order = ""
        self.plant_order = ""
        self.plantProdlot = ""
        self.distrShipment = ""
        self.wholeShipment = ""
        self.plantShipment = ""
        sheet_ret.write(int(self.currentPeriod), 0, int(self.currentPeriod))
        sheet_distr.write(int(self.currentPeriod), 0, int(self.currentPeriod))
        sheet_whole.write(int(self.currentPeriod), 0, int(self.currentPeriod))
        sheet_plant.write(int(self.currentPeriod), 0, int(self.currentPeriod))
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_period(self, client, data):
        client.sendall(pickle.dumps(str(self.currentPeriod)))

    def handle_get_ret_lastperiod(self, client, data):
        client.sendall(pickle.dumps(self.ret_lastperiod))

    def handle_upd_ret_lastperiod(self, client, data):
        self.ret_lastperiod = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_inventorycosts(self, client, data):
        self.ret_inventorycosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_inventory(self, client, data):
        self.ret_inventory = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_backlogcosts(self, client, data):
        self.ret_backlogcosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_backlogtotal(self, client, data):
        self.ret_backlogtotal = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_costs(self, client, data):
        self.ret_costs = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_get_ret_inventorycosts(self, client, data):
        client.sendall(pickle.dumps(self.ret_inventorycosts))

    def handle_get_ret_inventory(self, client, data):
        client.sendall(pickle.dumps(self.ret_inventory))

    def handle_get_ret_backlogcosts(self, client, data):
        client.sendall(pickle.dumps(self.ret_backlogcosts))

    def handle_get_ret_backlogtotal(self, client, data):
        client.sendall(pickle.dumps(self.ret_backlogtotal))

    def handle_get_ret_costs(self, client, data):
        client.sendall(pickle.dumps(self.ret_costs))

    def handle_get_distr_inventorycosts(self, client, data):
        client.sendall(pickle.dumps(self.distr_inventorycosts))

    def handle_get_distr_inventory(self, client, data):
        client.sendall(pickle.dumps(self.distr_inventory))

    def handle_get_distr_backlogcosts(self, client, data):
        client.sendall(pickle.dumps(self.distr_backlogcosts))

    def handle_get_distr_backlogtotal(self, client, data):
        client.sendall(pickle.dumps(self.distr_backlogtotal))

    def handle_get_distr_costs(self, client, data):
        client.sendall(pickle.dumps(self.distr_costs))

    def handle_get_distr_lastperiod(self, client, data):
        client.sendall(pickle.dumps(self.distr_lastperiod))

    def handle_upd_distr_lastperiod(self, client, data):
        self.distr_lastperiod = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_distr_inventorycosts(self, client, data):
        self.distr_inventorycosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_distr_inventory(self, client, data):
        self.distr_inventory = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_distr_backlogcosts(self, client, data):
        self.distr_backlogcosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_distr_backlogtotal(self, client, data):
        self.distr_backlogtotal = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_distr_costs(self, client, data):
        self.distr_costs = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_get_whole_inventorycosts(self, client, data):
        client.sendall(pickle.dumps(self.whole_inventorycosts))

    def handle_get_whole_inventory(self, client, data):
        client.sendall(pickle.dumps(self.whole_inventory))

    def handle_get_whole_backlogcosts(self, client, data):
        client.sendall(pickle.dumps(self.whole_backlogcosts))

    def handle_get_whole_backlogtotal(self, client, data):
        client.sendall(pickle.dumps(self.whole_backlogtotal))

    def handle_get_whole_costs(self, client, data):
        client.sendall(pickle.dumps(self.whole_costs))

    def handle_get_whole_lastperiod(self, client, data):
        client.sendall(pickle.dumps(self.whole_lastperiod))

    def handle_upd_whole_lastperiod(self, client, data):
        self.whole_lastperiod = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_whole_inventorycosts(self, client, data):
        self.whole_inventorycosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_whole_inventory(self, client, data):
        self.whole_inventory = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_whole_backlogcosts(self, client, data):
        self.whole_backlogcosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_whole_backlogtotal(self, client, data):
        self.whole_backlogtotal = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_whole_costs(self, client, data):
        self.whole_costs = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_get_plant_inventorycosts(self, client, data):
        client.sendall(pickle.dumps(self.plant_inventorycosts))

    def handle_get_plant_inventory_raw(self, client, data):
        client.sendall(pickle.dumps(self.plant_inventory_raw))

    def handle_get_plant_inventory_finished(self, client, data):
        client.sendall(pickle.dumps(self.plant_inventory_finished))

    def handle_get_plant_backlogcosts(self, client, data):
        client.sendall(pickle.dumps(self.plant_backlogcosts))

    def handle_get_plant_backlogtotal(self, client, data):
        client.sendall(pickle.dumps(self.plant_backlogtotal))

    def handle_get_plant_costs(self, client, data):
        client.sendall(pickle.dumps(self.plant_costs))

    def handle_get_plant_lastperiod(self, client, data):
        client.sendall(pickle.dumps(self.plant_lastperiod))

    def handle_upd_plant_lastperiod(self, client, data):
        self.plant_lastperiod = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_plant_inventorycosts(self, client, data):
        self.plant_inventorycosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_plant_inventory_raw(self, client, data):
        self.plant_inventory_raw = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_plant_inventory_finished(self, client, data):
        self.plant_inventory_finished = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_plant_backlogcosts(self, client, data):
        self.plant_backlogcosts = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_plant_backlogtotal(self, client, data):
        self.plant_backlogtotal = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

    def handle_upd_plant_costs(self, client, data):
        self.plant_costs = data.data_leadtimeup
        client.sendall(pickle.dumps(""))

server_class = SocketServer(HOST, PORT)
server_class.register_handler("get_adm", server_class.handle_get_adm)
server_class.register_handler("get_ret", server_class.handle_get_ret)
server_class.register_handler("get_distr", server_class.handle_get_distr)
server_class.register_handler("get_whole", server_class.handle_get_whole)
server_class.register_handler("get_plant", server_class.handle_get_plant)
server_class.register_handler("check_status", server_class.handle_check_status)
server_class.register_handler("check_status_node", server_class.handle_check_status_node)
server_class.register_handler("ret_order", server_class.handle_ret_order)
server_class.register_handler("distr_order", server_class.handle_distr_order)
server_class.register_handler("whole_order", server_class.handle_whole_order)
server_class.register_handler("plant_prodlot", server_class.handle_plant_prodlot)
server_class.register_handler("plant_order", server_class.handle_plant_order)
server_class.register_handler("upd_ret_cust_demand", server_class.handle_upd_ret_cust_demand)
server_class.register_handler("upd_ret_distr_demand", server_class.handle_upd_ret_distr_demand)
server_class.register_handler("upd_distr_whole_demand", server_class.handle_upd_distr_whole_demand)
server_class.register_handler("upd_whole_plant_demand", server_class.handle_upd_whole_plant_demand)

server_class.register_handler("distr_shipment", server_class.handle_distr_shipment)
server_class.register_handler("whole_shipment", server_class.handle_whole_shipment)
server_class.register_handler("plant_shipment", server_class.handle_plant_shipment)

server_class.register_handler("upd_ret_distr_shipment", server_class.handle_upd_ret_distr_shipment)
server_class.register_handler("upd_distr_whole_shipment", server_class.handle_upd_distr_whole_shipment)
server_class.register_handler("upd_whole_plant_shipment", server_class.handle_upd_whole_plant_shipment)
server_class.register_handler("add_status_ret", server_class.handle_add_status_ret)
server_class.register_handler("add_status_distr", server_class.handle_add_status_distr)
server_class.register_handler("add_status_whole", server_class.handle_add_status_whole)
server_class.register_handler("disconnect", server_class.handle_disconnect)
server_class.register_handler("set_period", server_class.handle_set_period)
server_class.register_handler("set_demand", server_class.handle_set_demand)
server_class.register_handler("upd_ret_period", server_class.handle_upd_ret_period)
server_class.register_handler("upd_ret_inventorycosts", server_class.handle_upd_ret_inventorycosts)
server_class.register_handler("upd_ret_inventory", server_class.handle_upd_ret_inventory)
server_class.register_handler("upd_ret_backlogcosts", server_class.handle_upd_ret_backlogcosts)
server_class.register_handler("upd_ret_backlogtotal", server_class.handle_upd_ret_backlogtotal)
server_class.register_handler("upd_ret_costs", server_class.handle_upd_ret_costs)
server_class.register_handler("get_ret_inventorycosts", server_class.handle_get_ret_inventorycosts)
server_class.register_handler("get_ret_inventory", server_class.handle_get_ret_inventory)
server_class.register_handler("get_ret_backlogcosts", server_class.handle_get_ret_backlogcosts)
server_class.register_handler("get_ret_backlogtotal", server_class.handle_get_ret_backlogtotal)
server_class.register_handler("get_ret_costs", server_class.handle_get_ret_costs)
server_class.register_handler("get_ret_lastperiod", server_class.handle_get_ret_lastperiod)
server_class.register_handler("upd_ret_lastperiod", server_class.handle_upd_ret_lastperiod)

server_class.register_handler("get_distr_inventorycosts", server_class.handle_get_distr_inventorycosts)
server_class.register_handler("get_distr_inventory", server_class.handle_get_distr_inventory)
server_class.register_handler("get_distr_backlogcosts", server_class.handle_get_distr_backlogcosts)
server_class.register_handler("get_distr_backlogtotal", server_class.handle_get_distr_backlogtotal)
server_class.register_handler("get_distr_costs", server_class.handle_get_distr_costs)
server_class.register_handler("get_distr_lastperiod", server_class.handle_get_distr_lastperiod)
server_class.register_handler("upd_distr_lastperiod", server_class.handle_upd_distr_lastperiod)
server_class.register_handler("upd_distr_inventorycosts", server_class.handle_upd_distr_inventorycosts)
server_class.register_handler("upd_distr_inventory", server_class.handle_upd_distr_inventory)
server_class.register_handler("upd_distr_backlogcosts", server_class.handle_upd_distr_backlogcosts)
server_class.register_handler("upd_distr_backlogtotal", server_class.handle_upd_distr_backlogtotal)
server_class.register_handler("upd_distr_costs", server_class.handle_upd_distr_costs)

server_class.register_handler("get_whole_inventorycosts", server_class.handle_get_whole_inventorycosts)
server_class.register_handler("get_whole_inventory", server_class.handle_get_whole_inventory)
server_class.register_handler("get_whole_backlogcosts", server_class.handle_get_whole_backlogcosts)
server_class.register_handler("get_whole_backlogtotal", server_class.handle_get_whole_backlogtotal)
server_class.register_handler("get_whole_costs", server_class.handle_get_whole_costs)
server_class.register_handler("get_whole_lastperiod", server_class.handle_get_whole_lastperiod)
server_class.register_handler("upd_whole_lastperiod", server_class.handle_upd_whole_lastperiod)
server_class.register_handler("upd_whole_inventorycosts", server_class.handle_upd_whole_inventorycosts)
server_class.register_handler("upd_whole_inventory", server_class.handle_upd_whole_inventory)
server_class.register_handler("upd_whole_backlogcosts", server_class.handle_upd_whole_backlogcosts)
server_class.register_handler("upd_whole_backlogtotal", server_class.handle_upd_whole_backlogtotal)
server_class.register_handler("upd_whole_costs", server_class.handle_upd_whole_costs)

server_class.register_handler("get_plant_inventorycosts", server_class.handle_get_plant_inventorycosts)
server_class.register_handler("get_plant_inventory_raw", server_class.handle_get_plant_inventory_raw)
server_class.register_handler("get_plant_inventory_finished", server_class.handle_get_plant_inventory_finished)
server_class.register_handler("get_plant_backlogcosts", server_class.handle_get_plant_backlogcosts)
server_class.register_handler("get_plant_backlogtotal", server_class.handle_get_plant_backlogtotal)
server_class.register_handler("get_plant_costs", server_class.handle_get_plant_costs)
server_class.register_handler("get_plant_lastperiod", server_class.handle_get_plant_lastperiod)
server_class.register_handler("upd_plant_lastperiod", server_class.handle_upd_plant_lastperiod)
server_class.register_handler("upd_plant_inventorycosts", server_class.handle_upd_plant_inventorycosts)
server_class.register_handler("upd_plant_inventory_raw", server_class.handle_upd_plant_inventory_raw)
server_class.register_handler("upd_plant_inventory_finished", server_class.handle_upd_plant_inventory_finished)
server_class.register_handler("upd_plant_backlogcosts", server_class.handle_upd_plant_backlogcosts)
server_class.register_handler("upd_plant_backlogtotal", server_class.handle_upd_plant_backlogtotal)
server_class.register_handler("upd_plant_costs", server_class.handle_upd_plant_costs)
server_class.register_handler("upd_plant_suppl_shipment", server_class.handle_upd_plant_suppl_shipment)
server_class.register_handler("upd_plant_produce_shipment", server_class.handle_upd_plant_produce_shipment)

server_class.accept_connections()
