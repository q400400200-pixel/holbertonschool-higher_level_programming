#!/usr/bin/python3
import logging


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendee dicts."""

    # Validate input types
    if not isinstance(template, str):
        logging.error(f"Invalid input type: template must be str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        logging.error(f"Invalid input type: attendees must be list, got {type(attendees).__name__}.")
        return

    # Ensure attendees is a list of dictionaries
    if not all(isinstance(item, dict) for item in attendees):
        bad_types = [type(item).__name__ for item in attendees if not isinstance(item, dict)]
        logging.error(f"Invalid input type: attendees must be a list of dictionaries, got {bad_types}.")
        return

    # Handle empty inputs
    if template == "":
        logging.error("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    # Placeholders to replace
    keys = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee and write output files
    for idx, attendee in enumerate(attendees, 1):
        filled = template

        for key in keys:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            filled = filled.replace("{" + key + "}", str(value))

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(filled)
        except OSError as e:
            logging.error(f"Error writing to file {filename}: {e}")
