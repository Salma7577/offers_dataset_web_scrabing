# offers_dataset_web_scrabing

this Repository contains the dataset for weekly offers booklets images.all the images are being labeled in YOLO format with the following classes:
offer_box: the whole surrounding bounding box of a single offer in a booklet
old_costs: the bounding box of the old cost that belongs to the first offer_box above it in the ".txt" file of the booklet page
new_costs: the bounding box of the new cost that belongs to the first offer_box above it in the ".txt" file of the booklet page
offers_name_arabic: the bounding box of the offer name in arabic  that belongs to the first offer_box above it in the ".txt" file of the booklet page
offers_name_english: the bounding box of the offer name in english that belongs to the first offer_box above it in the ".txt" file of the booklet page
quantity: the bounding box of the quantity that belongs to the first offer_box above it in the ".txt" file of the booklet page

## Page sample of the Pandah booklets
![image](https://user-images.githubusercontent.com/54520739/184260615-679e4c6f-3895-4a9e-9f79-dc3f3f108dc5.png)

## classes that belongs to the offer_box class
![image](https://user-images.githubusercontent.com/54520739/184260702-065788ef-7220-4c0b-ae78-4e1df0d58366.png)


source: https://www.alsoouq.com/
