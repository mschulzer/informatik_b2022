from projekt.models import Student, Report, StudentAdd,

def add_report(request):
    if request.method == 'POST':
        form = ReportAdd(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/ms@brgym.dk')

    else:
        form = ReportAdd()

    return render(request, "add_report.html", { 'form': form })
