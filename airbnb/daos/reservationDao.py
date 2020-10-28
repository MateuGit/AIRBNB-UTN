from reservations.models import Reservation

def setReservationTotalPrice(reservation,daysAmount):
    reservation.totalPrice = round(reservation.ownership.dailyRate * daysAmount * 1.08 , 2)
    reservation.save()

def saveReservation(request,ownership):
    print('test')
    reservation = Reservation(clientName=request.POST['firstname'],clientLastName= request.POST['lastname'], 
    clientEmail= request.POST['email'], ownership=ownership)
    reservation.save()
    print('test paso')
    return reservation