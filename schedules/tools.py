from  .models import Schedule,Grade,Subject
import datetime
def Switch(grade,subject,date_given,date_submitted,catagory):
    if(grade):
        if(subject and date_given and date_submitted and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
                subject=Subject.objects.filter(subject=subject).first(),catagories=catagory,given_date=date_given,date_submitted=date_submitted
            )
            return data            
        elif(subject and date_given and date_submitted):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
                subject=Subject.objects.filter(subject=subject).first(),given_date=date_given,
                date_submitted=date_submitted
            )
            return data
        elif(subject and date_given and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
                subject=Subject.objects.filter(subject=subject).first(),given_date=date_given,
                catagories=catagory
            )
            return data
        elif(subject and date_submitted and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
                subject=Subject.objects.filter(subject=subject).first(),date_submitted=date_submitted,
                catagories=catagory
            )
            return data
        elif(subject and date_submitted):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
        subject=Subject.objects.filter(subject=subject).first()
            )
            return data
        elif(subject and date_given):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
            subject=Subject.objects.filter(subject=subject).first(),date_given=date_given
                )
            return data
        elif(subject and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
            subject=Subject.objects.filter(subject=subject).first(),catagories=catagory
                )
            return data
        elif(date_given and date_submitted):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),given_date=date_given,submit_date=date_submitted)
            return data
        elif(date_given and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),given_date=date_given,catagories=catagory)
            return data
        elif(catagory and date_submitted):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),catagories=catagory,date_submitted=date_submitted)
            return data
        elif(subject):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
            subject=Subject.objects.filter(subject=subject).first()
            )
            return data
        elif(date_given):
            print(date_given)
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),given_date=date_given)
            return data
        elif(date_submitted):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),submit_date=date_submitted)
            return data
        elif(catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),catagories=catagory)
            return data
        else:
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first())
            return data
    elif(subject):
        if(grade and date_given and date_submitted and catagory):
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first()
                ,grade=Grade.objects.filter(grade=grade).first()
                ,catagories=catagory,given_date=date_given,date_submitted=date_submitted
            )
            return data            
        elif(grade and date_given and date_submitted):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
                subject=Subject.objects.filter(subject=subject).first(),given_date=date_given,
                date_submitted=date_submitted
            )
            return data
        elif(grade and date_given and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
                subject=Subject.objects.filter(subject=subject).first(),given_date=date_given,
                catagories=catagory
            )
            return data
        elif(grade and date_submitted and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
                subject=Subject.objects.filter(subject=subject).first(),date_submitted=date_submitted,
                catagories=catagory
            )
            return data
        elif(grade and date_submitted):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
        subject=Subject.objects.filter(subject=subject).first()
            )
            return data
        elif(grade and date_given):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
            subject=Subject.objects.filter(subject=subject).first(),date_given=date_given
                )
            return data
        elif(grade and catagory):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade).first(),
            subject=Subject.objects.filter(subject=subject).first(),catagories=catagory
                )
            return data
        elif(date_given and date_submitted):
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first(),given_date=date_given,submit_date=date_submitted)
            return data
        elif(date_given and catagory):
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first(),given_date=date_given,catagories=catagory)
            return data
        elif(catagory and date_submitted):
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first(),catagories=catagory,date_submitted=date_submitted)
            return data
        elif(grade):
            data = Schedule.objects.filter(grade=Grade.objects.filter(grade=grade),
            subject=Subject.objects.filter(subject=subject).first()
            )
            return data
        elif(date_given):
            print(date_given)
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first(),given_date=date_given)
            return data
        elif(date_submitted):
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first(),submit_date=date_submitted)
            return data
        elif(catagory):
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first(),catagories=catagory)
            return data
        else:
            data = Schedule.objects.filter(subject=Subject.objects.filter(subject=subject).first())
            return data
    elif(catagory):
            data = Schedule.objects.filter(catagories=catagory)
            return data
    elif(date_given):
        data =Schedule.objects.filter(given_date=date_given)
        return data
    elif(date_submitted):
        data =Schedule.objects.filter(submit_date=date_submitted)
        return data
