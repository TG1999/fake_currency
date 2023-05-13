from matplotlib import pyplot as plt
import cv2
x = input("PLEASE ENTER IMAGE PATH: ")
image = cv2.imread(x)
faceCascade = cv2.CascadeClassifier('file.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minSize=(50,50)
)
max_val=8
i=0
counter = 5
rectangledrawer={
    'x':0,'y':0,'w':0,'h':0
}
for (x, y, w, h) in faces:
    j=counter/5
    roi_color = image[y:y + h, x:x + w]
    orb = cv2.ORB_create()
    (kp1, des1) = orb.detectAndCompute(roi_color, None)
    training_set=['face/100_gandhi.jpg','face/2000_gandhi.jpg','face/500_gandhi.jpg','face/200_gandhi.jpg','face/100_new_gandhi.jpg']
    for i in range(0, len(training_set)):
        counter = counter +1
        train_img = cv2.imread(training_set[i])
        (kp2, des2) = orb.detectAndCompute(train_img, None)
        bf = cv2.BFMatcher(cv2.NORM_L1,crossCheck=False)
        all_matches = bf.knnMatch(des1, des2, k=2)
        good = []
        for (m, n) in all_matches:
            if m.distance < 0.789 * n.distance:
                good.append([m])
        if len(good) > max_val:
            max_val = len(good)
            rectangledrawer['x']=x
            rectangledrawer['y']=y
            rectangledrawer['w']=w
            rectangledrawer['h']=h
            max_pt = counter
            max_kp = kp2
            iteration = j
        print(counter, ' ', training_set[i], ' ', len(good))
point_of_interest=(max_pt-5)/iteration
if max_val > 50 :
    print(training_set[int(point_of_interest)-1])
    print('good matches ', max_val)
    print("CURRENCY MIGHT BE REAL, PLEASE CHECK FOR OTHER STEPS")
    cv2.rectangle(image, (rectangledrawer['x'], rectangledrawer['y']), (rectangledrawer['x']+rectangledrawer['w'], rectangledrawer['y']+rectangledrawer['h']), (0, 255, 0), 2)
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
    train_img = cv2.imread(training_set[int(point_of_interest)-1])
    img3 = cv2.drawMatchesKnn(roi_color, kp1, train_img, max_kp, good, 4)
    note = str(training_set[int(point_of_interest)-1]).split('.')
    note=note[0]
    (plt.imshow(img3), plt.show())
    plt.close()
else:
    cv2.imshow("img",image)
    cv2.waitKey(0)
    print("NO PORTRAIT DETECTED: CURRENCY MIGHT BE FAKE")