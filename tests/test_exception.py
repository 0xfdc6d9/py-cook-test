import logging

try:
    a = 5 / 0
except Exception as e:
    print()
    logging.info("okk")
    logging.error("Errors occurred during processing: " + e.__repr__())

