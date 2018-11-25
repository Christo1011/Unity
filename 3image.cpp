/*
  To compile this, do: g++ 3image.cpp
  To run: ./a.out input.png input2.png output.png
  Which will open input.png and input2.png,compare the colors using ditance formula and give back a black or white color, and save the result
  to output.png
*/
#include <iostream>
#include <math.h>
#include <vector>
#include "lodepng.cpp"

using namespace std;

int main(int argc, char* argv[]){
    
    if(argc < 4){
        cout << "I need 2 parameters, an input png and output png" << endl;
        return 1;
    }
    unsigned width, height,width1, height1;
    
    vector<unsigned char> image;
    vector<unsigned char> image1;
    //vector<unsigned char> image2;
    unsigned error = lodepng::decode(image, width, height, argv[1]);
    unsigned error1 = lodepng::decode(image1, width1, height1, argv[2]);
    //unsigned error2;
    if(error)cout << "Error! " << lodepng_error_text(error) << endl;
    if(error1)cout << "Error! " << lodepng_error_text(error1) << endl;
    
    cout << "Done loading!" << endl;
    cout << "Width: " << width << endl;
    cout << "Height: " << height << endl;
    
    cout << "Done loading!" << endl;
    cout << "Width: " << width1 << endl;
    cout << "Height: " << height1 << endl;
    
    for(int y = 0; y < height ; y++){
        for(int x = 0; x < width ; x++){
            unsigned tr = abs(image[(y * width + x) * 4 + 0] - image1[(y * width + x) * 4 + 0 ]);
            unsigned tb = abs(image[(y * width + x) * 4 + 1 ] - image1[(y * width + x) * 4 + 1 ]);
            unsigned tg = abs(image[(y * width + x) * 4 + 2 ] - image1[(y * width + x) * 4 + 2 ]);
            unsigned ta = sqrt((pow(tr,2)+pow(tb,2)+pow(tg,2))) * 255/(sqrt((pow(255,2)+pow(255,2)+pow(255,2))));
            
            image[(y * width + x) * 4 + 0] = ta;
            image[(y * width + x) * 4 + 1] = ta;
            image[(y * width + x) * 4 + 2] = ta;
            image[(y * width + x) * 4 + 3] = 255;
        }
    }
    error = lodepng::encode(argv[3], image, width, height);
    
    if(error)cout << "Error! " << lodepng_error_text(error) << endl;
    
    return 0;
}
