class image_process:

    def apiResponse(image):

        import requests
        import json

        url = "https://plant.id/api/v3/identification"
        payload = json.dumps({
        "images": [
            image
        ],
        "latitude": 49.207,
        "longitude": 16.608,
        "similar_images": True
        })
        headers = {
        'Api-Key': 'ZdPRBs91IuAJcSYVQWbkD3hjkEJZ2HJ3n4WijqrRPSUgUBLBbK',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        json_result = response.text

        data = json.loads(json_result)

        
        suggestions = data['result']['classification']['suggestions']
        best_suggestion = max(suggestions, key=lambda x: x['probability'])
        best_name = best_suggestion['name']

        return best_name

