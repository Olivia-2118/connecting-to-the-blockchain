import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJlMzU0MjJhZi1hNDhjLTRhMTQtOGYzNS0zMjg2ZjE1ZTg5MDMiLCJlbWFpbCI6ImxpbWVpY0BzZWFzLnVwZW5uLmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJiMWNlMTRiY2FiYzQxNjdkY2M1OSIsInNjb3BlZEtleVNlY3JldCI6IjRmZmYwYjM2YTJkNGU2MWFjYTM2NzkzNjUxZDNlYzBmN2M3NDFhNmNkODYwOWEyZTlhNGM3MTYwZWRhNjkwMTAiLCJleHAiOjE3OTIzODI2MTJ9.KykTLsn-3qWhVpit-agZbxgD6DQ4AA-y-kp_VKAXhRw"
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	headers = {
		"Authorization": f"Bearer {JWT_TOKEN}",
		"Content-Type": "application/json"
	}

	response = requests.post(url, headers=headers, json=data)
	assert response.status_code == 200, (
		f"Failed to pin to IPFS: {response.status_code}, {response.text}"
	)

	cid = response.json()["IpfsHash"]
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)
	assert response.status_code == 200, (
		f"Failed to get data from IPFS: {response.status_code}, {response.text}"
	)

	if content_type == "json":
		data = response.json()
	else:
		data = {"raw": response.text}

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
