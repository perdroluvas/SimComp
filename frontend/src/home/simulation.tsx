import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
} from "@/components/ui/form";

export default function Simulation() {
  const navigate = useNavigate();
  const form = useForm({
    defaultValues: {
      simulationTime: "",
      stepSize: "",
    },
  });

  function onSubmit(values) {
    console.log(values);
    navigate("/result");
  }

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-4">Simulation</h1>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          <FormField
            name="simulationTime"
            control={form.control}
            rules={{ required: "Simulation time is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Simulation Time (s)</FormLabel>
                <FormControl>
                  <input type="number" placeholder="Enter simulation time" {...field} />
                </FormControl>
                <FormDescription>Please enter the simulation duration in seconds.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            name="stepSize"
            control={form.control}
            rules={{ required: "Step size is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Step Size (s)</FormLabel>
                <FormControl>
                  <input type="number" placeholder="Enter step size" {...field} />
                </FormControl>
                <FormDescription>Please enter the simulation step size in seconds.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <div className="flex gap-4">
            <Button variant="outline" onClick={() => navigate("/network")}>
              Back
            </Button>
            <Button type="submit">Next: View Results</Button>
          </div>
        </form>
      </Form>
    </div>
  );
}
