
#include "server.h"
#include <iostream>
#include "StudentManager.h"
#include <cstdlib>  // system()

int main() {

    //cmd to html
    //Server svr;
    //svr.start();
    
    //test
    //StudentManager manager;
    //manager.processData();
    //std::cout << "按任意键退出程序...\n";
    //std::cin.get();  // 等待用户按下回车键

     // 直接运行 EmotionCat.exe 可执行文件
    const char* command = "..\\py\\dist\\EmotionCat.exe";  // 使用正确的路径

    // 执行命令
    int result = system(command);

    if (result == 0) {
        std::cout << "程序执行成功！" << std::endl;
    }
    else {
        std::cout << "程序执行失败！" << std::endl;
    }
    // 等待用户按键，防止闪退
    system("pause");

    return 0;
}

