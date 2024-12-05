<script>
    import IconBar from "$lib/visuals/IconBar.svelte";    
    import { onMount } from "svelte";
  
    export let totalBilling = 4636543; 
    let currentBilling = 0; 
    let formattedBilling = "0 €"; 

    let billingOptions = [
        { label: "Total", value: totalBilling, percentage: 37.5 },
        { label: "City", value: 3459980, percentage: 42.2 },
        { label: "Resort", value: 1176563, percentage: 28.0 }
    ];


    export let totalCancellations = 44010;
    let currentCancellations = 0; 

    let cancellationOptions = [
        { label: "Total", value: totalCancellations },
        { label: "City", value: 32972 },
        { label: "Resort", value: 11038 }
    ];

    let selectedBilling = billingOptions[0]; // Default to totalBilling
    let selectedCancellations = cancellationOptions[0]; // Default to totalCancellations


    let percentage = parseFloat(selectedBilling.percentage); // Reactive percentage

    function updateValues(option) {
        selectedBilling = billingOptions.find(opt => opt.label === option.label);
        selectedCancellations = cancellationOptions.find(opt => opt.label === option.label);

        // Animate counters
        animateCounter(selectedBilling.value, "billing");
        animateCounter(selectedCancellations.value, "cancellations");

        // Update percentage
        percentage = parseFloat(selectedBilling.percentage);
    }
    onMount(() => {
        animateCounter(selectedBilling.value, "billing");
        animateCounter(selectedCancellations.value, "cancellations");
    });

    function animateCounter(targetValue, type) {
        const duration = 500; 
        const start = performance.now();
        let initialValue = type === "billing" ? currentBilling : currentCancellations;

        function animate(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1); 
            if (type === "billing") {
                currentBilling = Math.round(initialValue + progress * (targetValue - initialValue)); 
                formattedBilling = new Intl.NumberFormat("es-ES", {
                    style: "currency",
                    currency: "EUR",
                    minimumFractionDigits: 0, 
                    maximumFractionDigits: 0, 
                }).format(currentBilling); 
            } else if (type === "cancellations") {
                currentCancellations = Math.round(initialValue + progress * (targetValue - initialValue));
            }

            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        }

        requestAnimationFrame(animate);
    }

</script>

<div class="flex  min-h-screen">
    <div class="flex flex-col w-1/2">
        <div class="flex flex-col items-center justify-center h-1/2">
            <p class=" font-semibold text-8xl">{currentCancellations.toLocaleString("es-ES")}</p>
            <p class="text-[#96DBC9] font-semibold text-xl mt-0">cancelled hotel reservations</p>
            <div class="flex items-center justify-center">
                <IconBar {percentage} />
                <p class="items-center justify-center mb-5 ml-5 flex">{selectedBilling.percentage} %</p>
            </div>
        </div>        
        <div class="flex items-center justify-center space-x-4 mt-4">
            {#each billingOptions as option}
                <button 
                    class="px-4 py-2 rounded border transition-all duration-200 
                           {option === selectedBilling ? 'bg-[#96DBC9] text-white' : 'bg-white text-[#96DBC9]'}"
                    on:click={() => updateValues(option)}
                >
                    {option.label}
                </button>
            {/each}
        </div>

        <div class="flex flex-col items-center justify-center h-1/2">
    
            <p class="text-8xl font-semibold">{formattedBilling}</p>
            <p class="text-[#96DBC9] font-semibold text-xl mt-0">billing loss due to cancellations</p>

            <!-- Clickable labels for billing and cancellations -->
        </div>
    </div>
    <div class="flex bg-[#96DBC9] flex-col w-1/2">
        <h1 class="p-8">The problem of hotel reservations cancellations</h1>
        <p class="pl-8 pr-8 text-gray-500 items-center justify-center mt-4 flex text-xl">
            Every year, thousands of hotel reservations are cancelled affecting the operation and the income of the hotels
        </p>
        <p class="pl-8 pr-8 text-gray-500 items-center justify-center mt-4 flex text-xl">
            One of the most relevant features to classify the cancellations is the type of hotel: City hotels and resorts have a different behaviour in terms of cancellations
        </p>

    </div>
</div>
