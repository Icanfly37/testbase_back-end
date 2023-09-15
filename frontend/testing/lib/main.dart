import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart'as http;


void main() async{
  var op = api_operator();
  op.sendExcelFile("D:/excel_test/test.xlsx");
  String path_target = "C:/Users/icanfly37/Desktop/testexcelrecieve/";
  op.downloadExcel("${path_target}sample_excel.xlsx");
  var geter = await op.getdata(); 
  print(geter);
}

class api_operator{
  Future<void> sendExcelFile(String path) async {
    try {
      // Replace with the URL of your API endpoint
      final apiUrl = Uri.parse('http://127.0.0.1:8000/files/');
      
      // Replace with the path to your Excel file
      String excelFilePath = path;
      final request = http.MultipartRequest('POST', apiUrl);
      request.files.add(await http.MultipartFile.fromPath('file', excelFilePath));
      final response = await request.send();
      if (response.statusCode == 200) {
        // File uploaded successfully
        print('File uploaded successfully');
      } else {
        // File upload failed
        print('File upload failed with status code: ${response.statusCode}');
      }
      Timer(Duration(milliseconds: 200), () { // delay time to end function
        exit(0);
      });
    } catch (e) {
      // Handle errors
      print('Error: $e');
    }
  }

  Future<void> downloadExcel(String path_for_export) async {
    final response = await http.post(Uri.parse('http://127.0.0.1:8000/uploadfile/'));

    if (response.statusCode == 200) {
      // final appDocDir = await getApplicationDocumentsDirectory();
      // final excelFilePath = '${appDocDir.path}/sample_excel.xlsx';
      String excelFilePath = path_for_export;

      // Save the downloaded file to the app's documents directory
      final file = File(excelFilePath);
      await file.writeAsBytes(response.bodyBytes);

      // Handle the downloaded file as needed, e.g., open it with a plugin or display it.
    } else {
      throw Exception('Failed to download Excel file');
    }
  }

  Future<Map<dynamic, dynamic>> getdata() async{
    final url = Uri.parse('http://127.0.0.1:8000/test'); // Replace with your FastAPI endpoint
    final response = await http.post(url);

    if (response.statusCode == 200) {
      // If the server returns a 200 OK response, parse the JSON data
      final jsonData = json.decode(response.body);
      // Process the data as needed
      // print(jsonData);
      return jsonData;
    } else {
      // If the server did not return a 200 OK response, throw an exception
      throw Exception('Failed to load data');
    }
  }
}

