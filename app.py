from flask import Flask, jsonify, request
from mysql.connector import connect, Error


try:
    connection = connect(
        host="localhost",
        user="root",
        password=""

    )
