void bug()
{
    //theory
    //√w^2 + (l + h)^2 = minimum
    //3d pythagoras
    int length, width, height;
    std::cout << "Enter length: ";
    std::cin >> length;
    std::cout << "\nEnter width: ";
    std::cin >> width;
    std::cout << "\nEnter height: ";
    std::cin >> height;
    
    
    float ret = sqrt(pow(width, 2) + pow((length + height), 2));
    std::cout << "Minimum distance is: " << ret << std::endl;
    
    //done
}