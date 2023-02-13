import os
from glob import glob
import numpy as np
import matplotlib.pyplot as plt 
from tqdm import tqdm
import pickle

for dataset in ['dataset1', 'dataset2', 'dataset3']:
    for partition in ['train', 'val', 'test']:

        img_names = glob(os.path.join(os.getcwd(), f'{dataset}/{partition}/*.jpg'))

        im = plt.imread(img_names[0])
        images = np.empty(shape=(len(img_names), im.shape[0], im.shape[1], im.shape[2]), dtype='uint8') 

        print(f'Loading {dataset} {partition}...')
        for (i, name) in tqdm(enumerate(img_names)):
            im = plt.imread(name)
            images[i] = im

        labels = [0 if 'cat' in name else 1 for name in img_names]

        image_label_pairs = [(images[i], labels[i]) for i in range(len(labels))]

        pickle.dump(image_label_pairs, open(f'{dataset}_{partition}.pkl','wb'),protocol=pickle.HIGHEST_PROTOCOL)