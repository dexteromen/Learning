package handlers

import (
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/google/uuid"

	"example.com/tasks/models"
)

// CreateTask handles the POST request to create a new task
func CreateTask(c *gin.Context) {
	var task models.Task
	if err := c.ShouldBindJSON(&task); err != nil {
		log.Println("Error binding JSON:", err)
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	if task.DueDate != "" {
		dueDate, err := time.Parse("2006-01-02", task.DueDate)
		if err != nil {
			log.Println("Error parsing DueDate:", err)
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid DueDate format: 2006-01-02"})
			return
		}
		task.DueDate = dueDate.Format("2006-01-02")
	}

	task.ID = uuid.New().String()
	task.CreatedAt = time.Now()
	task.UpdatedAt = time.Now()

	if err := models.CreateTask(task); err != nil {
		if err.Error() == "task with the same title already exists" {
			c.JSON(http.StatusConflict, gin.H{"error": err.Error()})
		} else {
			log.Println("Error creating task:", err)
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		}
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": "The task has been created", "task": task})
}

// GetTasks handles the GET request to retrieve all tasks
func GetTasks(c *gin.Context) {
	tasks, err := models.GetTasks()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, tasks)
}

// GetTask handles the GET request to retrieve a task by its ID
func GetTask(c *gin.Context) {
	id := c.Param("id")
	task, err := models.GetTaskByID(id)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Task not found"})
		return
	}
	c.JSON(http.StatusOK, task)
}

// UpdateTask handles the PUT request to update a task by its ID
func UpdateTask(c *gin.Context) {
	id := c.Param("id")
	var task models.Task
	task, err := models.GetTaskByID(id)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Task not found"})
		return
	}

	if err := c.ShouldBindJSON(&task); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	task.ID = id
	task.UpdatedAt = time.Now()

	if err := models.UpdateTask(task); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, task)
}

// UpdateTaskStatus handles the PUT request to update the status of a task by its ID
func UpdateTaskStatus(c *gin.Context) {
	id := c.Param("id")
	var request struct {
		Status string `json:"status"`
	}

	if err := c.ShouldBindJSON(&request); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	if err := models.UpdateTaskStatus(id, request.Status); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "Task status updated successfully"})
}

// DeleteTask handles the DELETE request to delete a task by its ID
func DeleteTask(c *gin.Context) {
	id := c.Param("id")
	_, err := models.GetTaskByID(id)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Task Not Found!"})
		return
	}

	if err := models.DeleteTask(id); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "Task deleted successfully"})
}
