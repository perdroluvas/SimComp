import * as React from "react"
import { useForm } from "react-hook-form"
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
} from "@/components/ui/form" // Adjust the import path as needed
import { useNavigate } from "react-router-dom"
import { Button } from "@/components/ui/button"

export default function Physical() {
  const navigate = useNavigate()

  // Initialize the form with default values
  const form = useForm({
    defaultValues: {
      height: "",
      weight: "",
    },
  })

  // Handle form submission
  function onSubmit(values) {
    console.log(values)
    navigate("/network")
  }

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-4">Physical Configuration</h1>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          {/* Height Field */}
          <FormField
            name="height"
            control={form.control}
            rules={{ required: "Height is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Height (cm)</FormLabel>
                <FormControl>
                  <input type="number" placeholder="Enter your height" {...field} />
                </FormControl>
                <FormDescription>
                  Please enter your height in centimeters.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Weight Field */}
          <FormField
            name="weight"
            control={form.control}
            rules={{ required: "Weight is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Weight (kg)</FormLabel>
                <FormControl>
                  <input type="number" placeholder="Enter your weight" {...field} />
                </FormControl>
                <FormDescription>
                  Please enter your weight in kilograms.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Submit Button */}
          <Button type="submit">Next: Network Configuration</Button>
        </form>
      </Form>
    </div>
  )
}