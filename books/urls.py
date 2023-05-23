from django.urls import path
from books import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    
    path('home/',views.homeview),
    path('About/',views.Aboutview),
    path('Ourbooks/',views.Ourbooksview),
    path('spaces/',views.spacesview.as_view()),
    path('blog/',views.blogview),
    path('Blogs/',views.blogview1),
    path('faq/',views.faqview),
    path('category/<int:id>',views.categoryview),
    path('blogdetail/<int:id>',views.blogdetailview),
    path('contact/',views.contactview.as_view()),
    path('insertcontact/',views.insertcontact),
    path('insertsubscribe/',views.insertsubscribe),
    path('signup/',views.signup),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('loginuser/',views.loginuser),
    path('dashboard/',views.dashboardview),
    path('issuedbooks/',views.issuedbooksview),
    path('returnedbooks/',views.returnedbooksview),
    path('categorydetail/<int:id>',views.categorydetailview),
    path('issued/<int:id>',views.issuedview),
    path('insertbook/',views.insertbook),
    path('return/<int:id>',views.returnview),
    path('updatereturn/<int:id>',views.updatereturn),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
    # path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    # path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]