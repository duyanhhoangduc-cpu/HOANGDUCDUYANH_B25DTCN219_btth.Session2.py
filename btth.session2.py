from datetime import datetime

print("HỆ THỐNG ĐÁNH GIÁ BỆNH NHÂN")
patient_name = input("Nhập tên bệnh nhân: ").strip()
birth_year = int(input("Nhập năm sinh: "))
sick_days = int(input("Nhập số ngày bị bệnh: "))
body_temperature = float(input("Nhập nhiệt độ cơ thể : "))
medical_fee = float(input("Nhập chi phí khám: "))

current_year = datetime.now().year

if (
    patient_name == ""
    or birth_year < 1900
    or birth_year > current_year
    or sick_days < 0
    or body_temperature < 30
    or body_temperature > 45
    or medical_fee <= 0
):
    print("Dữ liệu nhập vào không hợp lệ")
else:
    patient_age = current_year - birth_year
    if body_temperature >= 39:
        health_status = "SỐT CAO"
    elif body_temperature >= 37.5:
        health_status = "SỐT NHẸ"
    else:
        health_status = "BÌNH THƯỜNG"

    if patient_age >= 65 or body_temperature >= 39:
        priority_level = "ƯU TIÊN CAO"
    else:
        priority_level = "KHÁM THƯỜNG"

    print(" KẾT QUẢ ĐÁNH GIÁ")
    print("Tên bệnh nhân:", patient_name)
    print("Tuổi:", patient_age)
    print("Số ngày bị bệnh:", sick_days)
    print("Nhiệt độ:", body_temperature, "°C")
    print("Chi phí khám:", medical_fee, "VNĐ")
    print("Tình trạng sức khỏe:", health_status)
    print("Mức độ ưu tiên:", priority_level)