import socket
import mysql.connector

# DNS 서버 정보
dns_host = '192.168.0.1'  # DNS 서버 IP 주소
dns_port = 53        # DNS 서버 포트 번호

# 데이터베이스 연결
try:
    mysql_connection = mysql.connector.connect(
        host="localhost",
        user="yun",
        password="1224",
        db="socket"
    )
    print("데이터베이스 연결 성공")
except mysql.connector.Error as e:
    print("데이터베이스 연결 오류:", str(e))

def create_dns_table():
    cursor = mysql_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS domain_ip (
            id INT AUTO_INCREMENT PRIMARY KEY,
            domain VARCHAR(255) NOT NULL,
            ip_address VARCHAR(45) NOT NULL
        )
    """)
    mysql_connection.commit()
    cursor.close()

def handle_dns_query(connection, client_address):
    data = connection.recv(1024)
    query_type, query_content = data.decode().split(maxsplit=1)
    print(query_type)
    print(query_content)

    if query_type == 'N':
        # 데이터베이스에서 IP 주소 검색
        cursor = mysql_connection.cursor()
        query = "SELECT ip_address FROM domain_ip WHERE domain = %s"
        values = (query_content,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()

        if result is not None:
            ip_address = result[0]
        else:
            ip_address = "해당 도메인의 IP 주소를 찾을 수 없습니다."
        response = ip_address

    elif query_type == 'R':
        # 데이터베이스에서 도메인 검색
        cursor = mysql_connection.cursor()
        query = "SELECT domain FROM domain_ip WHERE ip_address = %s"
        values = (query_content,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()

        if result is not None:
            domain = result[0]
        else:
            domain = "해당 IP의 도메인을 찾을 수 없습니다."
        response = domain

    elif query_type == 'W':
        domain, ip_address = query_content.split()
        # 데이터베이스에 등록
        cursor = mysql_connection.cursor()
        query = "INSERT INTO domain_ip (domain, ip_address) VALUES (%s, %s)"
        values = (domain, ip_address)
        try:
            cursor.execute(query, values)
            if cursor.rowcount == 1:
                mysql_connection.commit()
                print("데이터베이스에 등록 완료")
                response = f"{domain} 도메인이 {ip_address} IP 주소와 함께 등록되었습니다."
            else:
                print("데이터베이스 등록 실패")
                response = "도메인 등록 중 오류가 발생했습니다."
        except Exception as e:
            error_message = f"도메인 등록 중 오류가 발생했습니다: {str(e)}"
            print(error_message)  # 서버의 콘솔에 에러 메시지 출력
            response = error_message
        finally:
            cursor.close()

    else:
        response = "잘못된 쿼리 유형을 받았습니다."
    
    # 응답 전송
    connection.send(response.encode())
    connection.close()
    return

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((dns_host, dns_port))
server_socket.listen(1)

create_dns_table()

while True:
    connection, client_address = server_socket.accept()
    print("클라이언트와 연결되었습니다.")
    handle_dns_query(connection, client_address)

server_socket.close()
