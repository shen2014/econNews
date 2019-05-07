
library(pdftools)

#input_data_dir <- "../download/savedownload2014_2019/savedownload2014_2019"
input_data_dir  <- "~/ml/econnews/download/savedownload2014_2019/savedownload2014_2019/"
output_data_dir <- "./2014_2019/"


file_name_list <- list.files(path = input_data_dir, pattern = "^fomcminutes.*pdf$")

print(file_name_list)

for (f_name in file_name_list){

	txt      <- pdf_text(paste(input_data_dir, f_name, sep = ""))

	n_pages  <- length(txt)

	print(paste(f_name, "has" , n_pages, "pages", sep = " "))

	for (i in 1:n_pages) {	
		
		page        <- txt[i]
		save_f_name <- paste(substr(f_name, 1, nchar(f_name) - 4), "page", i, sep = "_")
		save_f_name <- paste(save_f_name, "txt", sep = ".")
		save_f_name <- paste(output_data_dir, save_f_name, sep = "")
		save_file   <- file(save_f_name)
		cat(page, file = save_file)

	}
}
