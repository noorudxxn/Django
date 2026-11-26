from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

from io import BytesIO
from reportlab.pdfgen import canvas

from .forms import CertificateForm


def generate_certificate(request):

    if request.method == "POST":

        form = CertificateForm(request.POST)

        if form.is_valid():

            student_name = form.cleaned_data['student_name']
            course_name = form.cleaned_data['course_name']
            completion_date = form.cleaned_data['completion_date']
            email = form.cleaned_data['email']

            # Generate PDF
            buffer = BytesIO()

            p = canvas.Canvas(buffer)

            p.setTitle("Course Completion Certificate")

            p.setFont("Helvetica-Bold", 25)
            p.drawCentredString(
                300, 750,
                "CERTIFICATE OF COMPLETION"
            )

            p.setFont("Helvetica", 16)
            p.drawCentredString(
                300, 680,
                "This certificate is proudly presented to"
            )

            p.setFont("Helvetica-Bold", 24)
            p.drawCentredString(
                300, 620,
                student_name
            )

            p.setFont("Helvetica", 16)
            p.drawCentredString(
                300, 560,
                "For successfully completing the course"
            )

            p.setFont("Helvetica-Bold", 20)
            p.drawCentredString(
                300, 510,
                course_name
            )

            p.setFont("Helvetica", 14)
            p.drawCentredString(
                300, 440,
                f"Completion Date: {completion_date}"
            )

            p.setFont("Helvetica-Oblique", 14)
            p.drawCentredString(
                300, 350,
                "Congratulations on your achievement!"
            )

            p.showPage()
            p.save()

            pdf = buffer.getvalue()
            buffer.close()

            # Send email
            try:

                subject = "Course Completion Certificate"

                message = f"""
Dear {student_name},

Congratulations!

You have successfully completed the course: {course_name}.

Completion Date: {completion_date}

Thank you.
Training Institute
"""

                email_message = EmailMessage(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email]
                )

                email_message.attach(
                    "certificate.pdf",
                    pdf,
                    "application/pdf"
                )

                email_message.send(fail_silently=False)

                messages.success(
                    request,
                    "Certificate generated and email sent successfully!"
                )

            except Exception as e:

                messages.error(
                    request,
                    f"Certificate generated, but email failed: {e}"
                )

            # Download PDF
            response = HttpResponse(
                pdf,
                content_type='application/pdf'
            )

            response['Content-Disposition'] = (
                'attachment; filename="certificate.pdf"'
            )

            return response

    else:
        form = CertificateForm()

    return render(
        request,
        'classwork14/certificate_form.html',
        {'form': form}
    )