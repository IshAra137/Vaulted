from django.urls import path
from . import views
urlpatterns=[
    # Register and login
    path("signup", views.signup, name="signup"),
    path("login/", views.login, name="login"),

    # Welcome page after login
    path("welcome", views.welcome, name="welcome"),

    # Home
    path("aboutus", views.aboutus, name="aboutus"),
    path("home", views.home, name="home"),
    path("", views.home, name="home"),

    # Personal Data
    path("p", views.p, name="p"),
    path("personal", views.personal, name="personal"),
    path("personaldata", views.personaldata, name="personaldata"),
    path("pupdate/<int:a>", views.pupdate, name="pupdate"),
    path("pdelete/<int:a>", views.pdelete, name="pdelete"),
    path('psuccess/', views.psuccess, name='psuccess'),

    # Medical Data
    path("m", views.m, name="m"),
    path("medical", views.medical, name="medical"),
    path("medicaldata", views.medicaldata, name="medicaldata"),
    path("mupdate/<int:g>", views.mupdate, name="mupdate"),
    path("mdelete/<int:g>", views.mdelete, name="mdelete"),
    path('medsuccess/', views.medsuccess, name='medsuccess'),

    # Academic Data
    path("a", views.a, name="a"),
    path("academic", views.academic, name="academic"),
    path("academicdata", views.academicdata, name="academicdata"),
    path("aupdate/<int:p>", views.aupdate, name="aupdate"),
    path("adelete/<int:p>", views.adelete, name="adelete"),
    path('asuccess/', views.asuccess, name='asuccess'),

    # Financial Data
    path("f", views.f, name="f"),
    path("financial", views.financial, name="financial"),
    path("financialdata", views.financialdata, name="financialdata"),
    path("fupdate/<int:x>", views.fupdate, name="fupdate"),
    path("fdelete/<int:x>", views.fdelete, name="fdelete"),
    path('fsuccess/', views.fsuccess, name='fsuccess'),
    # Document Data
    path("d", views.d, name="d"),
    path("doc", views.doc, name="doc"),
    path("docdata", views.docdata, name="docdata"),
    path("dupdate/<int:u>", views.dupdate, name="dupdate"),
    path("ddelete/<int:u>", views.ddelete, name="ddelete"),
    path('docsuccess/', views.docsuccess, name='docsuccess'),
]