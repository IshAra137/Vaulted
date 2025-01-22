from django.shortcuts import render,redirect
from appv.models import logintable,registertable,personaltable,academictable,financialtable,medicaltable,Document
# Create your views here.

#register form
def signup(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]

        x = registertable(Name=a, Email=b, Type="User")
        x.save()
        q = logintable(Loginid=x,Name=a, Email=b,Type="User")
        q.save()
        return redirect('login')

    return render(request, "register.html")



#loginform
def login(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]

        q = registertable.objects.filter(Name=a).first()

        if q and q.Email == b and q.Type == "User":
            x = logintable.objects.get(Name=a)

            if x.Email == b:
                request.session["member_id"] = x.id
                return render(request, "welcome.html", {"name": x, "email": b})
        else: return render(request,"login_http.html")

    return render(request, "login.html")



#home
def home(request):
    return render(request,"home.html")



#welcome
def welcome(request):
    return render(request,"welcome.html")



#about us
def aboutus(request):
    return render(request,"aboutus.html")



#personal data page
def p(request):
    return render(request,"personal.html")

#personal http
def psuccess(request):
       return render(request,"p_http.html")

#add data
def personal(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]

        k = personaltable(Name=a, lastname=b, dob=c, age=d, address=e, Email=f, number=g)
        k.save()

        # Redirect to the success page after saving data
        return redirect('psuccess')

    return render(request, "pregister.html")

#show data
def personaldata(request):

    x = logintable.objects.get(id=request.session["member_id"])
    print(x.Name)
    c=personaltable.objects.filter(Name=x.Name).first()

    if request.method=="POST":
        c.Name = request.POST["name1"]
        c.lastname = request.POST["name2"]
        c.dob = request.POST["name3"]
        c.age = request.POST["name4"]
        c.address = request.POST["name5"]
        c.Email = request.POST["name6"]
        c.number = request.POST["name7"]
        c.save()

    return render(request, "pdata.html", {"personalkey": c})

#update personal data
def pupdate(request,a):
    a=personaltable.objects.get(id=a)
    if request.method == "POST":
     a.Name = request.POST["name1"]
     a.lastname = request.POST["name2"]
     a.dob = request.POST["name3"]
     a.age = request.POST["name4"]
     a.address = request.POST["name5"]
     a.Email = request.POST["name6"]
     a.number = request.POST["name7"]
     a.save()
     return redirect('personaldata')
    return render(request, "pregister.html", {"updatekey": a})


# delete
def pdelete(request,a):
    try:
        # Retrieve the medical record with the given ID
        record = personaltable.objects.get(id=a)
        record.delete()  # Delete the record

        # Redirect to the medical page after deletion
        return redirect('p')  # Adjust to the correct view you want to redirect to
    except personaltable.DoesNotExist:
        # Handle case where the record doesn't exist
        return redirect('p')  # or you can show an error message

#medical data
def m(request):
    return render(request,"medical.html")

#med http
def medsuccess(request):
       return render(request,"m_http.html")


#add m data
def medical(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        z = medicaltable(name=a, height=b, weight=c, blood_group=d, Gender=e, ill=f)
        z.save()

        # Redirect to the success page after saving data
        return redirect('medsuccess')

    return render(request, "mregister.html")


#show data
def medicaldata(request):

    z = logintable.objects.get(id=request.session["member_id"])
    print(z.Name)
    x=medicaltable.objects.filter(name=z.Name).first()

    if request.method=="POST":
        x.name = request.POST["name1"]
        x.height = request.POST["name2"]
        x.weight = request.POST["name3"]
        x.blood_group = request.POST["name4"]
        x.Gender = request.POST["name5"]
        x.ill = request.POST["name6"]
        x.save()

    return render(request, "mdata.html", {"medicalkey": x})

#update medical data
def mupdate(request,g):
    if request.method == "POST":
         g=medicaltable.objects.get(id=g)
         g.name = request.POST["name1"]
         g.height = request.POST["name2"]
         g.weight = request.POST["name3"]
         g.blood_group = request.POST["name4"]
         g.Gender = request.POST["name5"]
         g.ill = request.POST["name6"]
         g.save()

         # Redirect after saving
         return redirect('mdata')

         # Render the form with the current instance data
    return render(request, "mregister.html", {"updatekey": g})

#delete
def mdelete(request, g):
    try:
        # Retrieve the medical record with the given ID
        record = medicaltable.objects.get(id=g)
        record.delete()  # Delete the record

        # Redirect to the medical page after deletion
        return redirect('m')  # Adjust to the correct view you want to redirect to
    except medicaltable.DoesNotExist:
        # Handle case where the record doesn't exist
        return redirect('m')  # or you can show an error message


#academic data
def a(request):
    return render(request,"academic.html")

#a http
def asuccess(request):
       return render(request,"a_http.html")
#add data
def academic(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]

        k = academictable(Name=a, Hqul=b,  Passout=c, Degree=d, Spec=e, inst=f, addt=g)
        k.save()

        # Redirect to the success page after saving data
        return redirect('asuccess')

    return render(request, "aregister.html")

#show data
def academicdata(request):

    z = logintable.objects.get(id=request.session["member_id"])
    print(z.Name)
    x=academictable.objects.filter(Name=z.Name).first()

    if request.method=="POST":
        x.Name = request.POST["name1"]
        x.Hqul = request.POST["name2"]
        x.Passout = request.POST["name3"]
        x.Degree = request.POST["name4"]
        x.Spec = request.POST["name5"]
        x.inst = request.POST["name6"]
        x.addt = request.POST["name7"]
        x.save()

    return render(request, "adata.html", {"academickey": x})

#update academic data
def aupdate(request,p):
    p=academictable.objects.get(id=p)
    if request.method == "POST":
        p.Name = request.POST["name1"]
        p.Hqul = request.POST["name2"]
        p.Passout = request.POST["name3"]
        p.Degree = request.POST["name4"]
        p.Spec = request.POST["name5"]
        p.inst = request.POST["name6"]
        p.addt = request.POST["name7"]
        p.save()

    return render(request, "aregister.html", {"updatekey": p})


# delete
def adelete(request, p):
    try:
        # Retrieve the medical record with the given ID
        record = academictable.objects.get(id=p)
        record.delete()  # Delete the record

        # Redirect to the medical page after deletion
        return redirect('a')  # Adjust to the correct view you want to redirect to
    except academictable.DoesNotExist:
        # Handle case where the record doesn't exist
        return redirect('a')

#financial data
def f(request):
    return render(request,"financial.html")

#fin http
def fsuccess(request):
       return render(request,"f_http.html")
#add data
def financial(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]

        k = financialtable(Name=a, Bank_name=b,  Account_number=c, Account_type=d, Investments=e, Assets=f, Credit_score=g)
        k.save()

        # Redirect to the success page after saving data
        return redirect('fsuccess')

    return render(request, "fregister.html")

#show data
def financialdata(request):

    z = logintable.objects.get(id=request.session["member_id"])
    print(z.Name)
    x=financialtable.objects.filter(Name=z.Name).first()

    if request.method=="POST":
        x.Name = request.POST["name1"]
        x.Bank_name = request.POST["name2"]
        x.Account_number = request.POST["name3"]
        x.Account_type = request.POST["name4"]
        x.Investments = request.POST["name5"]
        x.Assets = request.POST["name6"]
        x.Credit_score = request.POST["name7"]
        x.save()

    return render(request, "fdata.html", {"financialkey": x})

#update financial data
def fupdate(request,x):
    x=financialtable.objects.get(id=x)
    if request.method == "POST":
        x.Name = request.POST["name1"]
        x.Bank_name = request.POST["name2"]
        x.Account_number = request.POST["name3"]
        x.Account_type = request.POST["name4"]
        x.Investments = request.POST["name5"]
        x.Assets = request.POST["name6"]
        x.Credit_score = request.POST["name7"]
        x.save()

    return render(request, "fregister.html", {"updatekey": x})

#  finance delete
def fdelete(request, x):
    try:
        # Retrieve the medical record with the given ID
        record = financialtable.objects.get(id=x)
        record.delete()  # Delete the record

        # Redirect to the medical page after deletion
        return redirect('f')  # Adjust to the correct view you want to redirect to
    except financialtable.DoesNotExist:
        # Handle case where the record doesn't exist
        return redirect('f')


# doc data
def d(request):
    return render(request, "docs.html")


# doc http
def docsuccess(request):
    return render(request, "d_http.html")


# add data
def doc(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Retrieve files from the request
        tenth_certificate = request.FILES.get('tenth_certificate')
        twelfth_certificate = request.FILES.get('twelfth_certificate')
        degree_certificate = request.FILES.get('degree_certificate')
        masters_certificate = request.FILES.get('masters_certificate')
        aadhar_card = request.FILES.get('aadhar_card')
        passport = request.FILES.get('passport')
        pan_card = request.FILES.get('pan_card')

        # Create and save a Document record
        document = Document.objects.create(
            name=name,
            tenth_certificate=tenth_certificate,
            twelfth_certificate=twelfth_certificate,
            degree_certificate=degree_certificate,
            masters_certificate=masters_certificate,
            aadhar_card=aadhar_card,
            passport=passport,
            pan_card=pan_card,
        )
        document.save()
        return redirect('docsuccess')


    return render(request, "dregister.html")


# show data
def docdata(request):
    # Retrieve all documents
    q = Document.objects.all()

    # Render the data in the 'ddata.html' template
    return render(request, "ddata.html", {"dockey": q})


# update doc data
def dupdate(request, u):
    u = Document.objects.get(id=u)
    if request.method == 'POST':
        # Update fields from form data
        u.name = request.POST.get('name', u.name)

        # Update files if a new file is uploaded
        if request.FILES.get('tenth_certificate'):
            u.tenth_certificate = request.FILES['tenth_certificate']
        if request.FILES.get('twelfth_certificate'):
            u.twelfth_certificate = request.FILES['twelfth_certificate']
        if request.FILES.get('degree_certificate'):
            u.degree_certificate = request.FILES['degree_certificate']
        if request.FILES.get('masters_certificate'):
            u.masters_certificate = request.FILES['masters_certificate']
        if request.FILES.get('aadhar_card'):
            u.aadhar_card = request.FILES['aadhar_card']
        if request.FILES.get('passport'):
            u.passport = request.FILES['passport']
        if request.FILES.get('pan_card'):
            u.pan_card = request.FILES['pan_card']

        u.save()  # Save the updated record
        return redirect('ddata')  # Redirect to the display page

    return render(request, "dregister.html", {"updatekey": u})


# delete
def ddelete(request, u):
    try:
        # Retrieve the document with the given ID
        record = Document.objects.get(id=u)
        record.delete()  # Delete the record

        # Redirect to the documents page after deletion
        return redirect('d')
    except Document.DoesNotExist:
        # Handle case where the record doesn't exist
        return redirect('d')


