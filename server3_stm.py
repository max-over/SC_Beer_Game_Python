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
        self.prod_order = 0
        self.currentPeriod = 0
        self.currentDemand = 0
        self.distrShipmentPlaced = 0
        self.distrShipmentTaken = 0
        self.distrShipment = 0
        self.wholeShipmentPlaced = 0
        self.wholeShipmentTaken = 0
        self.wholeShipment = 0
        self.plantShipmentPlaced = 0
        self.plantShipmentTaken = 0
        self.plantShipment = 0
        self.plantProdlot = 0
        self.shipment_ret_queue = []
        self.shipment_distr_queue = []
        self.shipment_whole_queue = []

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
                  f"Plant: Order: {self.prod_order} Shipment: {self.plantShipment}")
        client.sendall(pickle.dumps(status))

    def handle_check_status_node(self, client, data):
        orders = {"Retailer": self.ret_order, "Distr": self.distr_order, "Whole": self.whole_order,
                  "Plant": self.prod_order}
        shipments = {"Distr": self.distrShipment, "Whole": self.wholeShipment, "Plant": self.plantShipment}

        status = ""
        for name, order in orders.items():
            has_order = "yes" if order else "no"
            shipment = shipments.get(name, "")
            has_shipment = "yes" if shipment else "no"
            if name == "Retailer":
                status += f"{name}: order: {has_order}\n"
            else:
                status += f"{name}: order: {has_order} shipment: {has_shipment}\n"

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
        self.prod_order = data.data_leadtimeup
        print("plant order: " + str(self.prod_order))
        sheet_plant.write(int(self.currentPeriod), 2, int(self.prod_order))
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
        self.plantProdlot = data.data_leadtimeup
        print(f"plant prodlot: {self.plantProdlot}")
        sheet_plant.write(int(self.currentPeriod), 3, int(self.plantProdlot))
        wb.save(f'xlwt_example{self.port}_{xtime}.xls')
        client.sendall(pickle.dumps(""))

    def handle_upd_ret_distr_shipment(self, client, data):
        if self.distrShipmentTaken == 0:
            for row, (shipment, period) in enumerate(self.shipment_ret_queue):
                if int(period) == int(self.currentPeriod) - data.data_leadtimeup:
                    cz = shipment
                    #print(shipment)
                    break
                else:
                    cz = 0
            if len(self.shipment_ret_queue) > 20:
                self.shipment_ret_queue.pop(0)
        client.sendall(pickle.dumps(ProcessData("", cz, 0)))

    def handle_upd_distr_whole_shipment(self, client, data):
        if self.wholeShipmentTaken == 0:
            for row, (shipment, period) in enumerate(self.shipment_distr_queue):
                if int(period) == int(self.currentPeriod) - data.data_leadtimeup:
                    cz = shipment
                    #print(shipment)
                    break
                else:
                    cz = 0
            if len(self.shipment_distr_queue) > 20:
                self.shipment_distr_queue.pop(0)
        client.sendall(pickle.dumps(ProcessData("", cz, 0)))

    def handle_upd_whole_plant_shipment(self, client, data):
        if self.plantShipmentTaken == 0:
            for row, (shipment, period) in enumerate(self.shipment_whole_queue):
                if int(period) == int(self.currentPeriod) - data.data_leadtimeup:
                    cz = shipment
                    #print(shipment)
                    break
                else:
                    cz = 0
            if len(self.shipment_whole_queue) > 20:
                self.shipment_whole_queue.pop(0)
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
        self.distrShipmentTaken = 0
        self.wholeShipmentPlaced = 0
        self.wholeShipmentTaken = 0
        self.plantShipmentPlaced = 0
        self.plantShipmentTaken = 0
        self.ret_order = ""
        self.distr_order = ""
        self.whole_order = ""
        self.prod_order = ""
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
server_class.register_handler("plant_order", server_class.handle_plant_order)
server_class.register_handler("upd_ret_cust_demand", server_class.handle_upd_ret_cust_demand)
server_class.register_handler("upd_ret_distr_demand", server_class.handle_upd_ret_distr_demand)
server_class.register_handler("upd_distr_whole_demand", server_class.handle_upd_distr_whole_demand)
server_class.register_handler("upd_whole_plant_demand", server_class.handle_upd_whole_plant_demand)
server_class.register_handler("distr_shipment", server_class.handle_distr_shipment)
server_class.register_handler("whole_shipment", server_class.handle_whole_shipment)
server_class.register_handler("plant_shipment", server_class.handle_plant_shipment)
server_class.register_handler("plant_prodlot", server_class.handle_plant_prodlot)
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
server_class.accept_connections()
