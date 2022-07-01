#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def resume_curuculum (request):
  return HttpResponse ("""
<form method="post">
<input type="text">
<input type="text">
<input type="email" placeholder="email">
<input type="submit">
</form>
 """)

#member:malick diagne
#member:hamath diagne
