# Batch_code_detector
This is a project that detect, notify the ISHIDA KAWASHIMA packaging machine in real time whenever a pouch is packed without the batch code to reduce customer complaint.
Below are the two images of laminate attached to the packing machine. First image correponds to the laminate without any batchcode and second image represent the laminate with batch code. Initially the border of the batch code printing area is extracted by finding the four location of pixel that forms a rectangular region and region is cropped in the next stage. Next the sum of itensity of the cropped area is compared with the reference image with batchcode. If the intensity difference occurs then the image is considered as without batchcode. Once the laminate without batchcode is detected signal is passed onto the ISHIDA KAWASHIMA packing machine to stop, thereby preventing the without batchcode packcage and reducing the customer complaint.   

![img](https://github.com/Manojkl/Batch_code_detector/blob/master/images/snapshot15_86.jpg)

![img](https://github.com/Manojkl/Batch_code_detector/blob/master/images/snapshot15_20.jpg)
