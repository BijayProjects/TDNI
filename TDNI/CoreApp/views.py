from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Service, Portfolio, WhyChooseUs, Review, Contact


# ================= HOME PAGE =================
def home(request):
    """
    Render the home page with all dynamic content.
    """
    services = Service.objects.filter(is_active=True)
    portfolios = Portfolio.objects.filter(is_active=True)
    whychoose = WhyChooseUs.objects.filter(is_active=True)
    reviews = Review.objects.filter(is_approved=True)

    context = {
        "services": services,
        "portfolios": portfolios,
        "whychoose": whychoose,
        "reviews": reviews,
    }

    return render(request, "main/home.html", context)


# ================= CONTACT FORM =================
def submit_contact(request):
    """
    Handle contact form submission from the modal.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        service = request.POST.get("service", "")
        message = request.POST.get("message")

        if not name or not email or not message:
            messages.error(request, "Please fill in all required fields.")
            return redirect("home")

        Contact.objects.create(
            name=name,
            email=email,
            service=service,
            message=message
        )

        messages.success(request, "Thank you! Your message has been sent successfully.")
        return redirect("home")

    return redirect("home")


# ================= CLIENT REVIEW =================
def submit_review(request):
    """
    Handle client review submissions.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        company = request.POST.get("company", "")
        comment = request.POST.get("comment")
        rating = request.POST.get("rating", 5)

        if not name or not comment:
            messages.error(request, "Please provide your name and review.")
            return redirect("home")

        Review.objects.create(
            name=name,
            company=company,
            comment=comment,
            rating=rating,
            is_approved=False  # Admin approval required
        )

        messages.success(
            request,
            "Thank you! Your review has been submitted and will appear after approval."
        )
        return redirect("home")

    return redirect("home")
