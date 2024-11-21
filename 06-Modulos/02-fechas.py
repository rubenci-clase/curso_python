from datetime import datetime
import time
print(time.time())


fecha = datetime(2023, 1, 10)
print(fecha)

fecha = datetime.now()
print(fecha)

# crear fechas a partir de string
fechastr = datetime.strptime("2023-02-03", "%Y-%m-%d")
print(fechastr)
# tipos de directivas desde
# https://docs.python.org/3/library/datetime.html

# string a partir de una fecha
print(fecha.strftime("%Y-%m-%d"))
print(fecha.year,
      fecha.month,
      fecha.day,
      fecha.hour,
      fecha.minute
      )
