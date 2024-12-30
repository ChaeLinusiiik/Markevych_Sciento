from users.models import Student
from courses.models import Course
from base_sessions.models import Session
from payments.models import Payments

class System:
    @staticmethod
    def conduct_payment(Student: Student, amount: float, description: str) -> Payments:
        if Student.balance < amount:
            raise ValueError("Недостатньо коштів на балансі")
        
        payment = Payments.objects.create(
            user=Student,
            amount=amount,
            description=description,
            status="completed",
        )
        Student.balance -= amount
        Student.save()
        return payment
