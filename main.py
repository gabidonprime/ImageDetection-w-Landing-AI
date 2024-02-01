from landingai.pipeline.image_source import Webcam
from landingai.predict import Predictor

predictor = Predictor(  
    endpoint_id="3ba4838a-910b-4a62-a35f-54d506b2dead",
    api_key="land_sk_HQrb56SkzhT0E59Tbz4OL3DdfoF8Ji1KNz6zv0z89GmmMuyyC8",
)
with Webcam(fps=0.5) as webcam:
    for frame in webcam:
        # Resize and run predictions
        frame.resize(width=512) 
        frame.run_predict(predictor=predictor) 
        frame.overlay_predictions()
        print("------  Frame Captured  ------")

        # Check for car in preddictions
        if "Vehicle" in frame.predictions:
            print("Vehicle detected! :)")  

        # Check for disabled people 
        if "Disabled" in frame.predictions:
            print("Disabled person at bus stop. Bus driver prepare to assist.")

        if "Abled" in frame.predictions:
            print("Person detected at busstop. Prepare to stop.")
        