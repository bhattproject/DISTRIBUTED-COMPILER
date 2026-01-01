#include <bits/stdc++.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

#define PORT 5000
#define BUFFER 1024

// file_name -> list of peers (ip:port)
map<string, vector<string>> filePeers;

void handleClient(int clientSocket) {
    char buffer[BUFFER];
    memset(buffer, 0, BUFFER);

    read(clientSocket, buffer, BUFFER);
    string request(buffer);

    stringstream ss(request);
    string command;
    ss >> command;

    // UPLOAD <filename> <ip:port>
    if (command == "UPLOAD") {
        string filename, peer;
        ss >> filename >> peer;
        filePeers[filename].push_back(peer);
        string response = "UPLOAD SUCCESS\n";
        send(clientSocket, response.c_str(), response.size(), 0);
    }

    // DOWNLOAD <filename>
    else if (command == "DOWNLOAD") {
        string filename;
        ss >> filename;

        string response;
        if (filePeers.count(filename)) {
            for (auto &p : filePeers[filename]) {
                response += p + " ";
            }
            response += "\n";
        } else {
            response = "FILE NOT FOUND\n";
        }
        send(clientSocket, response.c_str(), response.size(), 0);
    }

    close(clientSocket);
}

int main() {
    int serverSocket, clientSocket;
    struct sockaddr_in serverAddr, clientAddr;
    socklen_t addrLen = sizeof(clientAddr);

    serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket < 0) {
        perror("Socket error");
        return 1;
    }

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        perror("Bind error");
        return 1;
    }

    listen(serverSocket, 10);
    cout << "Tracker running on port " << PORT << endl;

    while (true) {
        clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &addrLen);
        thread(handleClient, clientSocket).detach();
    }

    close(serverSocket);
    return 0;
}
