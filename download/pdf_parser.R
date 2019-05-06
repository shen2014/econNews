
library(pdftools)

file_name_list <- list.files(pattern = "*.pdf")

for (f_name in file_name_list){

	txt      <- pdf_text(f_name)

	n_pages  <- length(txt)

	print(paste(f_name, "has" , n_pages, "pages", sep = " "))

	for (i in 1:n_pages) {	
		
		page        <- txt[i]
		save_f_name <- paste(substr(f_name, 1, nchar(f_name) - 4), "page", i, sep = "_")
		save_f_name <- paste(save_f_name, "txt", sep = ".")
		save_file   <- file(save_f_name)
		cat(page, file = save_file)

	}
}
