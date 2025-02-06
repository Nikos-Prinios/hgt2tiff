import numpy as np
from PIL import Image
import argparse

def convert_hgt_to_tiff(input_hgt, output_tiff):
    data = np.fromfile(input_hgt, dtype='>i2')
    size = int(np.sqrt(data.size))
    data = data.reshape((size, size))
    
    data_normalized = ((data - data.min()) * (255.0 / (data.max() - data.min()))).astype(np.uint8)
    
    img = Image.fromarray(data_normalized)
    img.save(output_tiff)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert HGT file to TIFF')
    parser.add_argument('input', help='Input HGT file')
    parser.add_argument('output', help='Output TIFF file')
    
    args = parser.parse_args()
    convert_hgt_to_tiff(args.input, args.output)
