import cv2

def probability_map(network_definition,pretrained_model, frame, in_size):
    net = cv2.dnn.readNetFromCaffe(network_definition, pretrained_model)
    input_width = in_size[0]
    input_height = in_size[1]
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (input_width, input_height),(0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()
    return output
