# importing module
import logging

# Create and configure logger
logging.basicConfig(
    filename="newfile.log", format="%(asctime)s %(message)s", filemode="w"
)


# create logger
logger = logging.getLogger("logger")
