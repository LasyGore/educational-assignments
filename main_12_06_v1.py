from multiprocessing import Process, Manager

def process_request(data, request):
    product, action, amount = request
    if product not in data:
        data[product] = 0
    if action == "receipt":
        data[product] += amount
    elif action == "shipment":
        if data[product] >= amount:
            data[product] -= amount
        else:
            data[product] = 0
    print(f"Processed request: {request}. Warehouse data: {data}")

def main():
    with Manager() as manager:
        warehouse_data = manager.dict()
        requests = [
            ("product1", "receipt", 100),
            ("product2", "receipt", 150),
            ("product1", "shipment", 30),
            ("product3", "receipt", 200),
            ("product2", "shipment", 50)
        ]

        processes = []
        for request in requests:
            p = Process(target=process_request, args=(warehouse_data, request))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()

        print('****************************************************************************')
        print("* Final warehouse data:", dict(warehouse_data),"*")
        print('****************************************************************************')

if __name__ == "__main__":
    main()