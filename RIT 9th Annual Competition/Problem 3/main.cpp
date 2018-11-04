void caesar()
{
    int shift;
    std::string text;
    
    std::cout << "Enter shift value (1-25): ";
    std::cin >> shift;
    
    if(shift > 25 || shift < 1)
    {
        std::cout << "\nPlease select a value between 1 and 25";
        return;
    }
    else{
        std::cout << "Enter plain text: ";
        std::cin >> text;
    
        std::string ret = "";
        for(int i = 0; i < text.capacity(); i++)
        {
            ret += text[i] + shift;
        }
        std::cout << "Encrypted text: " << ret;
    }
}