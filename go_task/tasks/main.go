package main

import (
	"log"

	"github.com/gin-gonic/gin"

	"example.com/tasks/handlers"
	"example.com/tasks/models"
)

func main() {
	err := models.ConnectDatabase()
	if err != nil {
		log.Fatal("failed to connect database")
	}

	err = models.AutoMigrate()
	if err != nil {
		log.Fatal("failed to migrate database")
	}

	r := gin.Default()

	r.POST("/tasks", handlers.CreateTask)
	r.GET("/tasks", handlers.GetTasks)
	r.GET("/tasks/:id", handlers.GetTask)
	r.PUT("/tasks/:id", handlers.UpdateTask)
	r.DELETE("/tasks/:id", handlers.DeleteTask)
	r.PUT("/tasks/:id/status", handlers.UpdateTaskStatus)

	r.Run()
}
