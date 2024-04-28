from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient,VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce
from sale import Sale
from saleDetail import SaleDetail


path, _ = os.path.split(os.path.abspath(__file__))
class CrudClients(ICrud):
    def create(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(yellow_color + "Registro de Cliente")
        gotoxy(2, 3)
        print(green_color + "Empresa: Corporación el Rosado RUC: 0876543294001")
        gotoxy(2, 4)
        print(purple_color + "Seleccione el tipo de cliente:")
        gotoxy(2, 5)
        print("1) Cliente Regular")
        gotoxy(2, 6)
        print("2) Cliente VIP")
        tipo_cliente = input("Seleccione una opción: ")

        if tipo_cliente == "1":
            print("Cliente Regular")
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            dni = input("Ingrese el DNI del cliente: ")
            card = input("¿El cliente tiene tarjeta de descuento? (s/n): ").lower() == "s"
            new_client = RegularClient(nombre, apellido, dni, card)
        elif tipo_cliente == "2":
            print("Cliente VIP")
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            dni = input("Ingrese el DNI del cliente: ")
            new_client = VipClient(nombre, apellido, dni)
        else:
            print("Opción inválida")
            return

        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read()
        clients.append(new_client.getJson())
        json_file.save(clients)
        print("Cliente registrado exitosamente!")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(blue_color + "Actualización de Cliente")
        gotoxy(2, 3)
        print(blue_color + "Empresa: Corporación el Rosado RUC: 0876543294001")
        dni = input("Ingrese el DNI del cliente que desea actualizar: ")
        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read()

        
        found = False
        updated_clients = []
        for client in clients:
            if client['dni'] == dni:
                found = True
                gotoxy(2, 5)
                print("Cliente encontrado:")
                gotoxy(2, 6)
                print(f"Nombre: {client['nombre']}")
                gotoxy(2, 7)
                print(f"Apellido: {client['apellido']}")
                gotoxy(2, 8)
                print(f"DNI: {client['dni']}")
                print()
                new_nombre = input("Ingrese el nuevo nombre del cliente (deje en blanco para mantener el mismo): ")
                new_apellido = input("Ingrese el nuevo apellido del cliente (deje en blanco para mantener el mismo): ")
                if new_nombre:
                    client['nombre'] = new_nombre
                if new_apellido:
                    client['apellido'] = new_apellido
            updated_clients.append(client)

        if found:
           
            json_file.save(updated_clients)
            print("Cliente actualizado exitosamente!")
        else:
            print("Cliente no encontrado.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(blue_color + "Eliminación de Cliente")
        gotoxy(2, 3)
        print(blue_color + "Empresa: Corporación el Rosado RUC: 0876543294001")
        dni = input("Ingrese el DNI del cliente que desea eliminar: ")
        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.read()

        filtered_clients = [client for client in clients if client['dni'] != dni]

        if len(filtered_clients) < len(clients):
            json_file.save(filtered_clients)
            print("Cliente eliminado exitosamente!")
        else:
            print("Cliente no encontrado.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90)
        gotoxy(2, 2)
        print("==" + " " * 34 + "Consulta de Cliente" + " " * 35 + "==")
        gotoxy(2, 4)
        dni = input("Ingrese DNI del cliente: ")
        json_file = JsonFile(path + '/archivos/clients.json')
        clients = json_file.find("dni", dni)

        if clients:
            client = clients[0]
            gotoxy(2, 6)
            print(f"Nombre: {client['nombre']}")
            gotoxy(2, 7)
            print(f"Apellido: {client['apellido']}")
            gotoxy(2, 8)
            print(f"DNI: {client['dni']}")
        else:
            print("Cliente no encontrado.")
        input("Presione una tecla para continuar...")
        
class CrudProducts(ICrud):
 
    def create(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(blue_color + "Registro de Producto")
        gotoxy(2, 3)
       
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock inicial del producto: "))
        
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()
        if products:
            
            new_id = max(product["id"] for product in products) + 1
        else:
            new_id = 1
        descripcion = nombre
        new_product = Product(new_id, descripcion, precio, stock)
        products.append(new_product.getJson())
        json_file.save(products)
        
        print("Producto registrado exitosamente!")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(blue_color + "Actualización de Producto")
        id_producto = int(input("Ingrese el ID del producto que desea actualizar: "))
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()
        found = False
        updated_products = []
        for product in products:
            if product['id'] == id_producto:
                found = True
                gotoxy(2, 4)
                print("Producto encontrado:")
                gotoxy(2, 5)
                print(f"ID: {product['id']}")
                gotoxy(2, 6)
                print(f"Descripción: {product['descripcion']}")
                gotoxy(2, 7)
                print(f"Precio: {product['precio']}")
                gotoxy(2, 8)
                print(f"Stock: {product['stock']}")
                print()
                new_descripcion = input("Ingrese la nueva descripción del producto (deje en blanco para mantener la misma): ")
                new_precio = input("Ingrese el nuevo precio del producto (deje en blanco para mantener el mismo): ")
                new_stock = input("Ingrese el nuevo stock del producto (deje en blanco para mantener el mismo): ")
                if new_descripcion:
                    product['descripcion'] = new_descripcion
                if new_precio:
                    product['precio'] = float(new_precio)
                if new_stock:
                    product['stock'] = int(new_stock)
            updated_products.append(product)

        if found:
            json_file.save(updated_products)
            print("Producto actualizado exitosamente!")
        else:
            print("Producto no encontrado.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(green_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(blue_color + "Eliminación de Producto")
        id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()

        filtered_products = [product for product in products if product['id'] != id_producto]

        if len(filtered_products) < len(products):
            json_file.save(filtered_products)
            print("Producto eliminado exitosamente!")
        else:
            print("Producto no encontrado.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90)
        gotoxy(2, 2)
        print("==" + " " * 34 + "Consulta de Producto" + " " * 35 + "==")
        gotoxy(2, 4)
        id_producto = int(input("Ingrese el ID del producto que desea consultar: "))
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.find("id", id_producto)

        if products:
            product = products[0]
            gotoxy(2, 6)
            print(f"ID: {product['id']}")
            gotoxy(2, 7)
            print(f"Descripción: {product['descripcion']}")
            gotoxy(2, 8)
            print(f"Precio: {product['precio']}")
            gotoxy(2, 9)
            print(f"Stock: {product['stock']}")
        else:
            print("Producto no encontrado.")
        input("Presione una tecla para continuar...")

class CrudSales(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni = validar.solo_numeros("Ingrese el DNI del cliente: ", "Error: Solo se permiten números", 23, 6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni", dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            return
        client = client[0]
        cli = RegularClient(client["nombre"], client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(red_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line)
            id_articulo = int(validar.solo_numeros("Ingrese el ID del artículo: ", "Error: Solo se permiten números", 15, 9 + line))
            json_file = JsonFile(path+'/archivos/products.json')
            products = json_file.find("id", id_articulo)
            if not products:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                product = products[0]
                product = Product(product["id"],product["descripcion"],product["precio"],product["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);quantity = int(validar.solo_numeros("Ingrese la cantidad: ", "Error: Solo se permiten números", 49, 9 + line))
                gotoxy(59,9+line);print(product.preci * quantity)
                sale.add_detail(product, quantity)
                gotoxy(76,4);print(round(sale.subtotal, 2))
                gotoxy(76,5);print(round(sale.discount, 2))
                gotoxy(76,6);print(round(sale.iva, 2))
                gotoxy(76,7);print(round(sale.total, 2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            last_invoice = invoices[-1]["factura"] + 1
            data = sale.getJson()
            data["factura"] = last_invoice
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(blue_color + "Modificación de Venta")
        gotoxy(2, 3)
        invoice_number = input("Ingrese el número de factura que desea modificar: ")
        json_file = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file.find("factura", int(invoice_number))
        # Crear una instancia de Sale con el cliente asociado a la venta

        if invoices:
            invoice = invoices[0]
            print("Venta encontrada:")
            print(f"Factura: {invoice['factura']}")
            print(f"Fecha: {invoice['Fecha']}")
            print(f"Cliente: {invoice['cliente']}")
            print(f"detalle: {invoice['detalle']}")
            print(f"Total: {invoice['total']}")
            sale = Sale()
            sale.load_from_json(invoice)
            
            while True:
                print("\nOpciones de modificación:")
                print("1) Agregar productos")
                print("2) Eliminar productos")
                print("3) Finalizar modificación")
                option = input("Seleccione una opción: ")
                if option == "1":
                    print("Agregar productos a la factura")
                    while True:
                        product_id = input("Ingrese el ID del producto que desea agregar (o '0' para salir): ")
                        if product_id == "0":
                            break
                            # Buscar el producto por su ID
                        product = Product.find(int(product_id))
                        if product:
                    # Agregar el producto al detalle de la factura
                            sale.details.append(SaleDetail(product, 1))
                            print("Producto agregado a la factura.")
                        else:
                            print("Producto no encontrado.")
                elif option == "2":
                    print("eliminar producto a la factura")
                    while True:
                        print("Eliminar producto de la factura")
                        product_id = input("Ingrese el ID del producto que desea eliminar (o '0' para salir): ")
                        if product_id == "0":
                            break
                        # Verificar si el producto está en la factura
                        product_found = False
                        for detail in sale.details:
                            if detail.product.id == int(product_id):
                                product_found = True
                                # Eliminar el producto del detalle de la factura
                                sale.details.remove(detail)
                                print("Producto eliminado de la factura.")
                                break
                        if not product_found:
                            print("Producto no encontrado en la factura.")
                elif option == "3":
                    print("Finalizando modificación...")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
            invoices[0] = sale.getJson()
            json_file.save(invoices)
            print("Modificación de venta realizada exitosamente!")    
        else:
            print("Venta no encontrada.")
        input("Presione una tecla para continuar...")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(2, 1)
        print(red_color + "=" * 90 + reset_color)
        gotoxy(2, 2)
        print(blue_color + "Eliminación de Venta")
        gotoxy(2, 3)
        invoice_number = input("Ingrese el número de factura que desea eliminar: ")
        json_file = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file.read()

        filtered_invoices = [invoice for invoice in invoices if invoice['factura'] != int(invoice_number)]

        if len(filtered_invoices) < len(invoices):
            json_file.save(filtered_invoices)
            print("Venta eliminada exitosamente!")
        else:
            print("Venta no encontrada.")
        input("Presione una tecla para continuar...")
        time.sleep(2)

    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(red_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Venta"+" "*35+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            print(f"Impresion de la Factura#{invoice}")
            print(invoices)
        else:    
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            print("Consulta de Facturas")
            for fac in invoices:
                print(f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}")
            
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), 
            invoices,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices))
            total_client = list(filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices))

            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            print("filter cliente: ",total_client)
            print(f"map Facturas:{totales_map}")
            print(f"              max Factura:{max_invoice}")
            print(f"              min Factura:{min_invoice}")
            print(f"              sum Factura:{tot_invoices}")
            print(f"              reduce Facturas:{suma}")
        x=input("presione una tecla para continuar...")    
    

#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()    
            menu_clients = Menu("Menu Cientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                crud_clients = CrudClients()
                crud_clients.create()
            elif opc1 == "2":
                crud_clients = CrudClients()
                crud_clients.update()
            elif opc1 == "3":
                crud_clients = CrudClients()
                crud_clients.delete()
            elif opc1 == "4":
                crud_clients = CrudClients()
                crud_clients.consult()
            print("Regresando al menu Clientes...")
            time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        while opc2 != '5':
            borrarPantalla()
            menu_products = Menu("Menu Productos", ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 20, 10)
            opc2 = menu_products.menu()

            if opc2 == "1":
                crud_products = CrudProducts()
                crud_products.create()
            
            elif opc2 == "2":
                crud_products = CrudProducts()
                crud_products.update()
            
            elif opc2 == "3":
                crud_products = CrudProducts()
                crud_products.delete()
            
            elif opc2 == "4":
                crud_products = CrudProducts()
                crud_products.consult()
                
            print("Regresando al menú Productos...")
            time.sleep(2)

    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
            elif opc3 == "2":
                sales.consult()
                time.sleep(2) 
            elif opc3 == "3":
                sales.update()
                
            elif opc3 == "4":
                sales.delete()
 
            print("Regresando al menu Principal...")
            time.sleep(2)            
borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()