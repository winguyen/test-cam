#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char* argv[])
{
    std::cout << "application started" << std::endl;

    cv::VideoCapture cap(0);

    if(!cap.isOpened())
    {
        std::cerr << "Error: Could not open camera." << std::endl;
        return -1;
    }

    cv::Mat frame;

    while(true)
    {
        cap >> frame;
        if(frame.empty())
        {
            std::cerr << "Error: Captured empty frame." << std::endl;
            break;
        }

        cv::imshow("Pi Camera Feed", frame);

        if(cv::waitKey(1) == 'q')
        {
            break;
        }
    }

    cap.release();
    cv::destroyAllWindows();

    return 0;
}
