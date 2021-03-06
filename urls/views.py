# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# -*- coding: utf-8 -*-

import urllib.parse ,http.client , json

def query(request,query):
	# **********************************************
	# *** Update or verify the following values. ***
	# **********************************************

	# Replace the subscriptionKey string value with your valid subscription key.
	subscriptionKey = "d3a822d8bf854a05b6f1807a8b870cae"

	# Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
	# search APIs.  In the future, regional endpoints may be available.  If you
	# encounter unexpected authorization errors, double-check this value against
	# the endpoint for your Bing Web search instance in your Azure dashboard.
	host = "api.cognitive.microsoft.com"
	path = "/bing/v7.0/search"

	term = "define "+query

	def BingWebSearch(search):
	    "Performs a Bing Web search and returns the results."

	    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
	    conn = http.client.HTTPSConnection(host)
	    query = urllib.parse.quote(search)
	    conn.request("GET", path + "?q=" + query, headers=headers)
	    response = conn.getresponse()
	    headers = [k + ": " + v for (k, v) in response.getheaders()
	                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
	    return headers, response.read().decode("utf8")

	if len(subscriptionKey) == 32:


	    headers, result = BingWebSearch(term)
	    return JsonResponse(json.dumps(json.loads(result), indent=4))

	else:
		return JsonResponse("contact admin.")