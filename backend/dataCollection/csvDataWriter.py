#Gets the list of video details for each and every channel and writes to the excel file
import xlsxwriter
import os
def writer(data, channelName):
    #excel file creation 
    path = os.path.abspath('data')
    workbook = xlsxwriter.Workbook(path + '\\Channel-' + channelName + '.xlsx')
    worksheet = workbook.add_worksheet(channelName)
    #writing the titles to the file
    worksheet.write(0, 0, 'Channel Category')
    worksheet.write(0, 1, 'Views')
    worksheet.write(0, 2, 'Likes')
    worksheet.write(0, 3, 'Dislikes')
    worksheet.write(0, 4, 'Comments')
    worksheet.write(0, 5, 'Publish Date')
        
    # Start from the first cell. Rows and columns are zero indexed.
    row = 1
    col = 0

    #writing the contents of the list to the excel file as rows
    for category,views,likes,dislikes,comments,publishDate in (data):
        worksheet.write(row, col,     category)
        worksheet.write(row, col + 1, views)
        worksheet.write(row, col + 2, likes)
        worksheet.write(row, col + 3, dislikes)
        worksheet.write(row, col + 4, comments)
        worksheet.write(row, col + 5, publishDate)
        row += 1

    workbook.close()

